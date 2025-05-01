import librosa
import scipy
import numpy as np
import wave
from pydub import AudioSegment
import os
import tempfile
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtCore import QUrl
from pydub.playback import play
import librosa
from audio_processing.envelope_processor import EnvelopePoint, Envelope, EnvelopeProcessor
from audio_processing.repeat_processor import Repeater
from audio_processing.correlator import Correlator

"""
Defines core audio-file operations and interactions with the UI
three sample types:
    - Original_Track_File : wraps original track, does beat/downbeat loading
    - Sample_File : wraps each extracted loop, applies ADSR envelopes, repeats it
    - Sonic_Sample_file : subclass for built-in Sonic Pi samples
Major calculations and audio manipulation (ADSR envelopes, repeating, correlation)
done using EnvelopeProcessor, Repeater and Correlator, respectively

"""

class Audio_File():
    """
    Base class for any audio file
    - ensures wav format
    - loads raw PCM via librosa into self.signal
    - stores timing, duration, and Qt media
    """
    def __init__(self, file, db=None, db_name=None):
        # if database and name given, stream into a temp file
        if db and db_name:
            temp = tempfile.NamedTemporaryFile(suffix=os.path.splitext(file)[1], delete=False)
            db.read_one_audio_file_name(db_name, temp, temp=True)
            self.file_path = temp.name
        else:
            self.file_path = os.path.abspath(file)

        # ensure wav
        if os.path.splitext(self.file_path)[1] != ".wav":
            self.convert_to_wav()
        
        # load full audio segment for playback and envelope
        self.sound = AudioSegment.from_wav(os.path.abspath(self.file_path))
        self.max_time = self.sound.duration_seconds
        self.max_vol = self.sound.max_dBFS
        
        self.media = QMediaContent(QUrl.fromLocalFile(self.file_path))
        
        #self.time = []
        #self.signal = []
        self.signal, self.frame_rate = librosa.load(self.file_path, sr=None, mono=True)
        self.time = np.linspace(0, self.max_time, num=len(self.signal))
        

    def get_waveform(self, progress_callback=None):
        """
        return time, amplitude tuple for plotting
        """
        return (self.time, self.signal)

    def convert_to_wav(self):
        """
        if file in mp3 format, write out same name.wav and change file path
        """
        sound = AudioSegment.from_mp3(self.file_path)
        temp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        new_path = temp.name
        #new_path = f"{os.path.splitext(self.file_path)[0]}.wav"
        #if not(os.path.exists(new_path)):
            #print(new_path)
        sound.export(new_path, format="wav")
        self.file_path = new_path

class Original_Track_File(Audio_File):
    """
    Represents the original track in the project
        - has downbeat list from the database
        - keeps project context and an Audio_Recogniser
    """
    def __init__(self, file, project_name, audio_recogniser, database):
        tempfile.NamedTemporaryFile
        super().__init__(file, db=database, db_name="full_track")
        self.tempo = librosa.feature.tempo(y=self.signal, sr=self.frame_rate, start_bpm=60)[0]
        
        self.condensed_signal = librosa.resample(y=self.signal, orig_sr=self.frame_rate, target_sr=self.frame_rate//4)
        self.condensed_time = np.linspace(0, self.max_time, num=len(self.condensed_signal))

        self.downbeats = database.get_downbeats()
        self.project_name=project_name
        self.audio_recogniser = audio_recogniser
    
    def get_waveform(self, progress_callback=None):
        """
        return downsampled waveform
        """
        return (self.condensed_time, self.condensed_signal)


class Sample_File(Audio_File):
    """
    single extracted loop
        - loads or generates its ADSR envelope
        - computes similarity via Correlator to the original track
        - finds offsets over threshold and repeats itself via Repeater
        - updates metadata stored in MongoDB if needed
    """
    def __init__(self, file=None, name=None, full_track=None, database=None, rank=0, env_set=False, database_name=None):
        if database_name is None:
            database_name = name
        
        super().__init__(file, db=database, db_name=database_name)
        self.name = name
        self.rank = rank
        self.database = database
        self.full_track = full_track
        self.checked = False
        self.enveloped_file = self.file_path
        self.repeated_file = None
        self.repeated_media = None
        self.offsets = []
        self.val_arr = []
        self.corr = [[],[]]

        # prep correlator using original track
        self.correlator = Correlator(
            self.full_track.signal,
            self.full_track.frame_rate,
            self.full_track.max_time,
            self.full_track.downbeats
        )

        # if this sample is in database
        # reload its envelope, correlation and minimum correlation threshold
        exists = self.database.file_exists(database_name)

        if exists:
            self._get_from_database(database_name)
            env_set = True
        else:
            # brand-new sample so no beat probs
            self.downbeat_probs = []
            original_vol = self.sound.max_dBFS
            self.min_corr = -1
            # initialise dummy envelope
            self.set_env_with_coordinates((0,0), (0,0), (0,0), (0,0), (0,0))

        # compute raw PCM and metadata
        self._raw_signal_calc()
        self.media = QMediaContent(QUrl.fromLocalFile(self.file_path))

        # default ADSR spanning whole sample
        self.first_sound = self.time[np.argmax(self.time > 0)]
        if env_set == False:
            start = (self.first_sound,0)
            attack = (self.first_sound,original_vol)
            decay = (self.first_sound,original_vol)
            sustain = (self.max_time,original_vol)
            release = (self.max_time,0)
            self.set_env_with_coordinates(start, attack, decay, sustain, release)
        
        # implement envelope
        self.env_processor = EnvelopeProcessor(self.sound)
        self.implement_envelope()

        # min/max corr for thresholding
        if len(self.corr[1]) > 0:
            if self.min_corr < 0:
                self.min_corr = np.max(self.corr[1]) - 0.001
                self.max_corr = self.min_corr + 0.1
                file_id = self.database.add_one_sample_file_with_env_list(self.name, self.file_path, self.get_envelope(), self.min_corr, [0 for i in range(len(self.time))])
            else:
                self.max_corr = np.max(self.corr[1]) + 0.099
        else:
            self.min_corr = 0
            self.max_corr = 0

        # compute offset list ad overlay repeats
        self.update_offsets()

        repeated_file_id = self.database.file_exists(f"{os.path.splitext(self.name)[0]}_repeated.wav")
        if repeated_file_id:
            #self.repeated_file =  self.get_repeated_sample_path()
            temp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
            self.repeated_file = temp.name
            self.database.read_one_audio_file_id(repeated_file_id, self.repeated_file)
            self.repeated_media = QMediaContent()
            self.repeated_media = QMediaContent(QUrl.fromLocalFile(self.repeated_file))
        else:
            self.sample_repeat()
    
    def _get_from_database(self, database_name):
        """
        retrieve envelope and similarity probabilities from database
        """
        #base, _ = os.path.split(self.file_path)
        #path = os.path.dirname(base)
        #self.file_path = self.get_full_vol_path(path)
        #self.database.read_one_audio_file_name(database_name, self.file_path)
        env = self.database.get_envelope(database_name)
        self.downbeat_probs = self.database.get_bar_probs(database_name)
        self._initialise_metadata()
        self.set_env_with_list(env)
        self.min_corr = self.database.get_min_corr(database_name)

    def _initialise_metadata(self):
        self.corr = self.correlator.beat_aligned(self.downbeat_probs)
    
    def _raw_signal_calc(self):
        """load raw PCM from file_path"""
        raw = wave.open(self.file_path)
        n_frames = raw.getnframes()
        frames = raw.readframes(n_frames)
        signal = np.frombuffer(frames, dtype=np.int16)
        n_channels = signal.size // n_frames
        signal = signal.reshape(n_frames, n_channels)
        self.signal = signal[:, 0]
        self.frame_rate = raw.getframerate()    
        self.time = np.linspace(0, n_frames/self.frame_rate, num=n_frames, endpoint=False)
        self.max_time = self.time[-1]
        self.max_vol = np.max(np.abs(self.signal))
        
    def get_full_vol_path(self, path):
        return os.path.join(path,"samples_full_vol",self.name)
    
    def increase_amplitude(self):
        """amplify audio file to have same volume as original track"""
        if self.sound.dBFS < self.full_track.sound.dBFS:
            self.sound = self.sound.apply_gain(self.full_track.sound.dBFS - self.sound.dBFS)
        base, _ = os.path.split(self.file_path)
        path = os.path.dirname(base)
        self.file_path = os.path.join(path, "samples_full_vol", self.name)
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.sound.export(self.file_path, format="wav")
    
    def set_min_corr(self, corr, progress_callback=None):
        """
        update similarity probability threshold
        and find new valid offsets for sample occurrences
        """
        if corr != self.min_corr:
            self.min_corr = corr
            self.update_offsets()
            self.sample_repeat()
    
    def get_envelope(self):
        """
        Returns:
            envelope as a tuple of ([x coords], [y coords])
        """
        env_coords = np.array([[p.time, p.level] for p in [self.env.start, self.env.attack, self.env.decay, self.env.sustain, self.env.release]])
        xs = env_coords[:,0]
        ys = env_coords[:,1]
        return (list(xs), list(ys))

    def set_env_with_list(self, env):
        """
        sets envelope

        Args:
            env : envelope as a tuple of ([x coords], [y coords])
        """
        self.env = Envelope(
            start = EnvelopePoint(env[0][0], env[1][0]),
            attack = EnvelopePoint(env[0][1], env[1][1]),
            decay = EnvelopePoint(env[0][2], env[1][2]),
            sustain = EnvelopePoint(env[0][3], env[1][3]),
            release = EnvelopePoint(env[0][4], env[1][4]),
        )
    
    def set_env_with_coordinates(self, start, attack, decay, sustain, release):
        """
        sets envelops

        Args:
            start, attack, decay, sustain, release : individual coordinates of envelope
        """
        self.env = Envelope(
            start = EnvelopePoint(start[0], start[1]),
            attack = EnvelopePoint(attack[0], attack[1]),
            decay = EnvelopePoint(decay[0], decay[1]),
            sustain = EnvelopePoint(sustain[0], sustain[1]),
            release = EnvelopePoint(release[0], release[1]),
        )

    def get_correlation(self, track, progress_callback=None):
        """
        Calculate full audio signal correlation between original file and sample file
        Gives noisy similarity measure

        Args:
            track : Original_File instance
        """
        sr_within = track.frame_rate
        try:
            y_find, _ = librosa.load(self.enveloped_file, sr=sr_within)
        except Exception as e:
            print(e)
            return ([],[])
        return self.correlator.full_correlation(y_find)
    
    def get_correlation_histogram(self, track, progress_callback=None):
        return self.correlator.get_correlation_histogram(track.downbeats)
        
    def update_offsets(self):
        """
        Find all sample occurrences in the track where the likelihood
        of that occurence is higher than the min_corr threshold.
        Generates x coords (offsets) and y_coords (val_arr) for green
        dots showing sample occurrences
        """
        if len(self.corr[1]) > 0:
            time, probs = self.corr[0], self.corr[1]
            if self.min_corr < 3:
                time, probs = self.correlator.downsample_corr(time, probs)
            self.offsets, self.val_arr = self.correlator.threshold(time, probs, self.min_corr)
        else:
            self.offsets = []
            self.val_arr = []

    def implement_envelope(self, path=None):
        """
        Apply ADSR and write to temp wav file
        """
        new_sound = self.env_processor.implement_envelope(self.env)
        if path == None:
            #base, _ = os.path.split(self.file_path)
            #path = os.path.dirname(base)
            #path = os.path.join(path, "enveloped_samples")
            temp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
            self.enveloped_file = temp.name
        else:
            self.enveloped_file = os.path.join(path, f"{os.path.splitext(self.name)[0]}_enveloped.wav")
            if os.path.exists(self.enveloped_file):
                os.remove(self.enveloped_file)
       
        new_sound.export(self.enveloped_file, format="wav")

        self.media = QMediaContent()
        self.media = QMediaContent(QUrl.fromLocalFile(self.enveloped_file))
        if len(self.offsets) != 0:
            self.sample_repeat()
        return self.media

    def get_repeated_sample_path(self):
        """not used after introduction of temporary files"""
        base, _ = os.path.split(self.file_path)
        path = os.path.dirname(base)
        path = os.path.join(path, "repeated_samples", f"{os.path.splitext(self.name)[0]}_repeated.wav")
        return path
    
    def sample_repeat(self):
        """
        overlay sample repeats into a temp file via Repeater
        """
        if self.enveloped_file != None:
            sample = AudioSegment.from_wav(self.enveloped_file)
        else:
            sample = AudioSegment.from_wav(self.file_path)
        #self.repeated_file = self.get_repeated_sample_path()
        temp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        self.repeated_file = temp.name
        
        repeater = Repeater(sample, self.offsets, self.full_track.max_time)
        repeater.export(self.repeated_file)
        
        file_id = self.database.add_repeat_sample_file(f"{os.path.splitext(self.name)[0]}_repeated.wav", self.repeated_file)
        self.repeated_media = QMediaContent()
        self.repeated_media = QMediaContent(QUrl.fromLocalFile(self.repeated_file))

class Sonic_Sample_File(Sample_File):
    """
    thin wrapper for built-in Sonic Pi samples
        - uppercase database name
        - use beat_aligned_sonic instead of beat_alligned
    """
    def __init__(self, file, name, full_track, database, rank):
        super().__init__(file, name, full_track, database, rank=rank, database_name=name.upper(), env_set=True)
        self.max_vol = 10000
    
    def _initialise_metadata(self):
        # sonic pi files has particular downbeats probs format in DB
        # due to different similarity measure
        self.corr = self.correlator.beat_aligned_sonic(self.downbeat_probs, self.full_track.time)

    """def implement_envelope(self, path=None):
        base, _ = os.path.split(self.full_track.file_path)
        current_project_path = os.path.dirname(base)
        path = os.path.join(current_project_path, "sonic_pi_samples")
        self.enveloped_file = os.path.join(path, f"{os.path.splitext(self.name)[0]}_enveloped.wav")
        return super().implement_envelope(path=path)"""
    
    """def increase_amplitude(self):
        if self.sound.dBFS < self.full_track.sound.dBFS:
            self.sound = self.sound.apply_gain(self.full_track.sound.dBFS - self.sound.dBFS)
        base, _ = os.path.split(self.full_track.file_path)
        current_project_path = os.path.dirname(base)
        path = os.path.join(current_project_path, "sonic_pi_samples")
        self.file_path = os.path.join(path, f"{os.path.splitext(self.name)[0]}_full_vol.wav")
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.sound.export(self.file_path, format="wav")
        pass"""
    
    def get_full_vol_path(self, path):
        return self.file_path

    def get_repeated_sample_path(self):
        base, _ = os.path.split(self.full_track.file_path)
        current_project_path = os.path.dirname(base)
        path = f"{current_project_path}/sonic_pi_samples"
        self.repeated_file = f"{path}/{os.path.splitext(self.name)[0]}_repeated.wav"
        return self.repeated_file
    
    def get_correlation_histogram(self, track, progress_callback=None):
        return (self.corr[0], self.corr[1])

    def update_offsets(self):
        """
        sonic Pi similarity measure more noisy so downsample first
        """
        if len(self.corr[1]) > 0:
            time, probs = self.corr[0], self.corr[1]
            time, probs = self.correlator.downsample_corr(time, probs)
            self.offsets, self.val_arr = self.correlator.threshold(time, probs, self.min_corr)
        else:
            self.offsets = []
            self.val_arr = []


        