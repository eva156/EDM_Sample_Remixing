from loopextractor.loopextractor.loopextractor.loopextractor import make_spectral_cube, validate_template_sizes, create_loop_spectrum, get_loop_signal
import os
import librosa
import soundfile
import tensorly.decomposition as tld
import numpy as np
import madmom
from pydub import AudioSegment
import gridfs
from io import BytesIO
from storage.audio_recogniser import Audio_Recogniser

"""
Implements LoopExtactor
    - loads audio file and detects downbeat times via madmom
    - segments the signal into bars and build spectral cube
    - applies non-negative Tucker decomposition via TensorLy
    - reconstruct individual loop components and writes them into GridFS
    - matches each separated loop against a library of Sonic Pi samples
    - stores extracted loops and matched samples with metadata in MongoDB
"""

class LoopExtractor:
    """
    Attributes:
        n_templates : [n_sounds, n_rhythms, n_loops] initial template counts
        audio_recogniser: helper to match separated loops to Sonic Pi samples
    """
    def __init__(self, n_templates=[0,0,0]):
        assert len(n_templates)==3
        assert type(n_templates) is list
        self.n_templates = n_templates
        self.audio_recogniser = Audio_Recogniser()
    
    def run_algorithm(self, audio_file, output_savename, output_folder, database, original_track_creation):
        """
        Loop extraction as implemented by loopextractor but with additional 
        database operations
        """
        assert os.path.exists(audio_file)
        # Load mono audio:
        signal_mono, fs = librosa.load(audio_file, sr=None, mono=True)
        # Use madmom to estimate the downbeat times:
        downbeat_times = self.get_downbeats(audio_file)
        print(downbeat_times)
        self.initialise_full_track_file(downbeat_times, audio_file, database)
        original_track_creation.emit(50)
        # Convert times to frames so we segment signal:
        downbeat_frames = librosa.time_to_samples(downbeat_times, sr=fs)
        #print(downbeat_times)
        # Create spectral cube out of signal:
        spectral_cube = make_spectral_cube(signal_mono, downbeat_frames)
        # Validate the input n_templates (inventing new ones if any is wrong):
        n_sounds, n_rhythms, n_loops = validate_template_sizes(spectral_cube, self.n_templates)
        # Use TensorLy to do the non-negative Tucker decomposition:
        core, factors = tld.non_negative_tucker(np.abs(spectral_cube), [n_sounds, n_rhythms, n_loops], n_iter_max=500, verbose=True)
        #sounds = factors[0]
        #rhythms = factors[1]
        #loops = factors[2]
        separated_loop_files = []
        # Reconstruct each loop:
        for ith_loop in range(n_loops):
            # Multiply templates together to get real loop spectrum:
            loop_spectrum = create_loop_spectrum(factors[0], factors[1], core[:,:,ith_loop])
            # Choose best bar to reconstruct from (we will use its phase):
            bar_ind, bar_probs = self.choose_bar_to_reconstruct(factors[2], ith_loop, loop_spectrum, spectral_cube)
            norm_bar_prob = (bar_probs - np.min(bar_probs)) / (np.max(bar_probs) - np.min(bar_probs))
            norm_bar_prob *= 100
            #print(norm_bar_prob)
            full_loop = self.estimate_source_signal(bar_probs, loop_spectrum, spectral_cube)
            #file = os.path.join(output_folder, f"separated_loop_{ith_loop}.wav")
            #soundfile.write(file, full_loop, fs)
            file = self.initialise_loop_file(database, full_loop, fs, ith_loop)
            separated_loop_files.append(file)
            #bar_probs = factors[2][:,:ith_loop]
            # Reconstruct loop signal by masking original spectrum:
            ith_loop_signal = get_loop_signal(factors[2][:,ith_loop][bar_ind]*loop_spectrum, spectral_cube[:,:,bar_ind])
            # Write signal to disk:
            soundfile.write("{0}_{1}.wav".format(output_savename,ith_loop), ith_loop_signal, fs)
            #print(downbeat_times[bar_ind])
            self.initialise_sample_file(10, norm_bar_prob, f"sample_{ith_loop}.wav", audio_file, database, "{0}_{1}.wav".format(output_savename,ith_loop), 0)
        track_length = librosa.get_duration(y=signal_mono, sr=fs)
        self.initialise_sonic_sample_files(database, separated_loop_files, track_length)

    def get_downbeats(self, file):
        """
        compute downbeat times using madmom's RNN and DBN
        Returns:
            list of timestamps where bar onsets occur
        """
        downbeats = np.array([])
        proc = madmom.features.downbeats.DBNDownBeatTrackingProcessor(beats_per_bar=[4],fps=100)
        act = madmom.features.downbeats.RNNDownBeatProcessor()(file)
        beats = proc(act)
        downbeats = [x[0] for x in beats if x[1]==1]
        
        return downbeats

    def choose_bar_to_reconstruct(self, loop_templates, ith_loop, loop_spectrum, spectral_cube):
        """
        Select the best bar index whose phase will be used for reconstruction
        Computes softmask-weighted loudness metric per bar
        (same as loopextractor except added the softmask weights)
        """
        loudness_time_softmask= []
        for b in range(len(loop_templates[:,:ith_loop])):
            original_spectrum = spectral_cube[:,:,b]
            min_length = np.min((loop_spectrum.shape[1], original_spectrum.shape[1]))
            orig_mag, orig_phase = librosa.magphase(original_spectrum)
            mask = librosa.util.softmask(loop_spectrum[:,:min_length], orig_mag[:,:min_length], power=1)
            loudness_time_softmask.append(loop_templates[:,ith_loop][b]*np.sum(mask))
        #bar_prev = np.argmax(loop_templates[:,ith_loop])
        bar_ind = np.argmax(loudness_time_softmask)
        #print(f"{bar_prev},{bar_ind}")
        return bar_ind, loop_templates[:,ith_loop]

    def estimate_source_signal(self, bar_probs, loop_spectrum, spectral_cube):
        """
        produce full loop time-domain signal
        """
        full_signal = []
        for b in range(len(bar_probs)):
            original_spectrum = spectral_cube[:,:,b]
            min_length = np.min((loop_spectrum.shape[1], original_spectrum.shape[1]))
            mag = loop_spectrum * bar_probs[b]
            orig_mag, orig_phase = librosa.magphase(original_spectrum)
            mask = librosa.util.softmask(mag[:,:min_length], orig_mag[:,:min_length], power=1)
            masked_spectrum = original_spectrum[:,:min_length] * mask
            signal = librosa.core.istft(masked_spectrum)
            full_signal.append(signal)
        loop_signal = np.concatenate(full_signal)
        return loop_signal
    
    def initialise_full_track_file(self, downbeats, file, database):
        """store the original track with doenbeat meta data"""
        database.add_full_track_file(file, downbeats)
    
    def write_sample_file(self, min_prob, bar_probs, name, database, rank, original_vol, sound):
        """
        stream AudioSegment into GridFS database and record metadata

        Args:
            min_prob:   min correlation threshold for sample
            bar_probs:  list of downbeat probabilities
            name:   name to store sample in database under
            database:   ProjectDatabase instance
            rank:   sample rank (always 0 for extracted loop)
            original_vol: original y coordinate for A,D,S of ADSR
            sound: AudioSegment instance for sample
        """
        buf = BytesIO()
        sound.export(buf, format="wav")
        buf.seek(0)
        max_time = sound.duration_seconds
        start = (0,0)
        attack = (0,original_vol)
        decay = (0,original_vol)
        sustain = (max_time,original_vol)
        release = (max_time,0)
        database.add_one_sample_file(name, buf, start, attack, decay, sustain, release, min_prob, list(bar_probs), rank, buf=True)
    
    def initialise_sample_file(self, min_prob, bar_probs, name, full_track, database, file, rank=0):
        """
        set extract loop to have same peak level as the full track
        and delete on-disk file then write sample to database

        Args:
            min_prob:   min correlation threshold for sample
            bar_probs:  list of downbeat probabilities
            name:   name to store sample in database under
            full_track: path for original track
            database:   ProjectDatabase instance
            fille:  path to temp wav file for sample
            rank:   sample rank (always 0 for extracted loop)
        """
        sound = AudioSegment.from_file(file)
        full_track_sound = AudioSegment.from_file(full_track)
        original_vol = sound.max
        if sound.dBFS < full_track_sound.dBFS:
            sound = sound.apply_gain(full_track_sound.dBFS - sound.dBFS)
        os.remove(file)
        sound.export(out_f=file, format="wav")

        self.write_sample_file(min_prob, bar_probs, name, database, rank, original_vol, sound)
            
    def initialise_loop_file(self, database, loop, fs, i):
        """
        write numpy array into in-memory buffer,
        and store as separated_loop_idx
        Returns:
            assigned file ID
        """
        buf = BytesIO()
        buf.name = "file.wav"
        soundfile.write(buf, loop, fs)
        buf.seek(0)
        file_id = database.add_source_separated_loop(f"separated_loop_{i}", buf)
        return file_id

    def initialise_sonic_sample_files(self, database, files, track_length):
        """
        match each separated loop against the Sonic Pi sample library
        then store the match locations and score of matches as new sample files
        """
        matched_sonic_samples = self.audio_recogniser.compare_separated_loops(track_length, database, file_ids = files)
        for i, s in enumerate(matched_sonic_samples.keys()):
            file = os.path.abspath(f"sample-pi-main/{s.lower()}")
            hist = matched_sonic_samples[s]
            min_prob = float(np.max(hist[1]))
            min_prob -= 0.5
            min_prob = max(0.5, min_prob)
            #print(min_prob)
            sound = AudioSegment.from_file(file)
            self.write_sample_file(min_prob, [list(hist[0]), list(hist[1])], s, database, i+1, sound.max, sound)

#l = LoopExtractor()
#l.run_algorithm("C:/Users/uno4e/OneDrive/Documents/Cambridge II/project/music/sax_ehrling.mp3", "", "", None, None)
