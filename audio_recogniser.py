from abracadabra import recognise, storage, fingerprint
import glob
import numpy as np
import taglib
import tempfile

"""
Provides Aufio_Recogniser, a high-level wrapper around the Abracadabra
fingerpring library and taglib for:
    - initialising and maintainging the fingerprinting DB
    - registering songs with ID3 tags
    - recognising whether a file exists in the DB
    - retrieving and scoring offset matches
    - ranking and histogramming matched samples
    - bulk-registering sonic pi built-in samples
    - comparing source separated tracks agains the Sonic Pi samples
"""

class Audio_Recogniser:
    """
    uses abracadabra.storage for the DB
    uses abracadabra.recognise for lookup & scoring
    """
    def __init__(self):
        """
        ensure fingerprint database set up
        """
        try:
            storage.setup_db()
        except Exception as e:
            print(f"ERROR could not set up fingerprint DB: {e}")
        #self.delete_data()
        #self.register_sonic_pi_samples()
    
    def exists_in_db(self, path):
        """
        Check if an audio file has already been fingerprinted 

        Args:
            path (str): path to the audio file
        Returns:
            bool:   True if song registered before
        """
        return recognise.song_in_db(path)
    
    def register_song(self, path, name, project):
        """ 
        Tag an audio file with TITLE/ALBUM metadata and register it

        Args:
            path (str): Path to the audio file
            name (str): Desired TITLE tag
            project (str): Desired ALBUM tage
        """
        try:
            self.set_song_tag(path, name, project)
        except Exception as e:
            print(f"ERROR could not write tags to {path}: {e}")
            return

        try:
            recognise.register_song(path)
        except Exception as e:
            print(f"ERROR could not register song {path} in fingerprint DB: {e}")
    
    def recognise_song(self, path):
        return recognise.recognise_song(path)

    def set_song_tag(self, path, name, project):
        """
        Overwrite TITLE and ALBUM tags in an audio file using TagLib

        Args:
            path (str): Path to the audio file
            title (str): TITLE tag value
            album (str): ALBUM tag value
        """
        with taglib.File(path, save_on_exit=True) as song:
            song.tags['TITLE'] = []
            del song.tags['TITLE']
            song.tags['TITLE'] = [name.upper()]
            song.tags['ALBUM'] = []
            del song.tags['ALBUM']
            song.tags['ALBUM'] = [project]
            #print(song.tags)
    
    def histogram(self, offsets, track_length):
        """
        Build a histogram of time-differences between matched offsets

        Args:
            offsets (list if (t1, t2)): pairs of matched timestamps
            track_length (float): Total track duration (seconds)
        Returns:
            [bins, counts]: Two lists for plotting the histogram
        """
        binwidth = 0.1
        # compute absolute time differences
        offsets = np.array(offsets)
        tks = np.abs(offsets[:,0] - offsets[:,1])
        #tks = list(map(lambda x: np.abs(x[0] - x[1]), offsets))
        hist, b = np.histogram(tks,
                            bins=np.arange(0,
                                            int(track_length + binwidth + 1),
                                            binwidth))
        #score = float(np.max(hist))
        hist = list(map(lambda x: int(x), hist))
        b = list(map(lambda x: float(x), b))
        return [b, hist]
    
    def get_offsets(self, path):
        """
        Fingerprint a file and fetch DB all matching sing IDs and offsets

        Uses abracadabra's Shazam-inspired fingerprint matcher:
            - fingerprint_file() produces pairs of spectral-peak hashes
            - get_matches() returns a dict song_id -> list of (track_time, sample_time)
            - score_match() builds a histrogram of time-difference deltas (track_time - sample_time)
              and returns the peak bin count normalised by total matches, i.e. the
              strongest alignment confidence

        Args:
            path (str): path to audio file
        Returns:
            dict: keys=(SONG_TITLE, ALBUM), values = (sorted_offsets, score, count)
            {} on any failure
        """
        try:
            hashes = fingerprint.fingerprint_file(path)
        except Exception as e:
            print(f"ERROR fingerprinting failed for {path}: {e}")
            return {}

        try:
            matches = storage.get_matches(hashes)
        except Exception as e:
            print(F"ERROR DB lookup failed for hashes from {path}: {e}")
            return {}
        
        song_matches = {}
        for song_id, offsets in matches.items():
            try:
                song = storage.get_info_for_song_id(song_id)
                offsets_new = np.sort([off[1] for off in offsets])
                score = recognise.score_match(offsets)
                song_matches[(song[1],song[2])] = (offsets_new, score, len(offsets_new))
            except Exception as e:
                print(F"WARNING skipping song_id={song_id}, error processing offsets: {e}")
        return song_matches
    
    def order_samples(self, matches_dict, offsets_dict, track_length):
        """
        Rank samples by match score and occurence count

        Args:
            matches_dict (dict): sample_name -> (offsets, score, count)
            offsets_dict (dict): sample_name -> offset_list
            track_length (float): duration for histogram binning
        
        Returns:
            dict: sample_name->[bins, counts], histogram, sorted by descending score
        """
        # build structured array for sorting
        dtype = [('name', object), ('score', float), ('occurences', int)]
        songs = list(matches_dict.values())
        ranked_songs = np.array(songs, dtype=dtype)
        # sort by score, then occurrences, then name
        ranked_songs = np.array(np.flip(np.sort(ranked_songs, order=['score', 'occurences', 'name'])))
        sample_dict = {s['name']: self.histogram(offsets_dict[s['name']], track_length) for s in ranked_songs}
        return sample_dict
    
    def match_sonic_samples(self, path, song_matches, offsets_dict):
        """
        Merge matches for built-in Sonic Pi samples into existing dicts

        for sample loop:
            - fingerprint it and retrieve matches
            - if it is a sonic pi sample, comput a Shazam-style score
            - accumulate scores and offsets to support ranking by both match count and alignment

        Args:
            path (str): sample file path to fingerprint
            song_matches (dict): existing sing_id -> (name, score, count)
            offsets_dict (dit): name -> offsets list
        Returns:
            (song_matches, offsets_dict)
        """
        try:
            hashes = fingerprint.fingerprint_file(path)
            matches = storage.get_matches(hashes)
        except Exception as e:
            print(f"ERROR cannot match {path}: {e}")
            return song_matches, offsets_dict
        
        for song_id, offsets in matches.items():
            try:
                song = storage.get_info_for_song_id(song_id)
                offsets_new = offsets
                score = recognise.score_match(offsets)
                # only process Sonic Pi registered entries
                if song[1] == "sonic-pi-samples":
                    prev_match = song_matches.get(song_id)
                    if prev_match != None:
                        score += prev_match[1]
                        len_offsets = prev_match[2] + len(offsets_new)
                        offsets_new = np.concatenate((offsets_dict[prev_match[0]], offsets_new))
                        song_matches[song_id] = (prev_match[0], score, len_offsets)
                        offsets_dict[prev_match[0]] = offsets_new
                    else:
                        song_matches[song_id] = (song[2], score, len(offsets_new))
                        offsets_dict[song[2]] = offsets_new
            except:
                print(f"WARNING could not merge match for song_id={song_id}: {e}")
        return song_matches, offsets_dict
    
    def delete_data(self):
        """
        Drop and recreate the fingerprint database tables
        """
        with storage.get_cursor() as (conn, c):
            c.execute("DROP TABLE IF EXISTS hash")
            c.execute("DROP TABLE IF EXISTS song_info")
        storage.setup_db()
    
    def get_data(self):
        """
        Fetch all entries from sing_info table

        Returns:
            list of tuples: raw database rows
        """
        with storage.get_cursor() as (conn, c):
            c.execute("SELECT * FROM song_info")
            return c.fetchall()
    
    def register_sonic_pi_samples(self):
        """
        Scan Sonic Pi samples folder and register each .wav file
        """
        files = glob.glob("C:\\Users\\uno4e\\OneDrive\\Documents\\Cambridge II\\project\\EDM_Sample_Remixing\\sample-pi-main\\*.wav")
        for f in files:
            name = f.split('\\')[-1]
            self.register_song(f, name, "sonic-pi-samples")
    
    def compare_separated_loops(self, track_length, database, project_path=None, file_ids=None):
        """
        Compare extracted loops against the sonic-pi DB and return histograms used to score them

        Args:
            track_length (float): Duration of the original track
            database (ProjectDatabase): for retrieving loop files
            project_path (str, optional): Base project folder for loops
            file_ids (list, optional): Pre-extract IDs of loop files in database
        Returns:
            dict: sample_name -> [bins, counts]
        """
        if project_path != None:
            try:
                files = database.get_separated_loop_tracks(f"{project_path}/loop_tracks")
            except Exception as e:
                print(f"ERROR could not fetch separated loops: {e}")
                return {}
        if file_ids != None:
            files = []
            for i in file_ids:
                temp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
                database.read_one_audio_file_id(i, temp, temp=True)
                files.append(temp.name)
        matched_songs = {}
        offsets = {}
        for f in files:
            matched_songs, offsets = self.match_sonic_samples(f, matched_songs, offsets)
        try:
            sample_dict = self.order_samples(matched_songs, offsets, track_length)
            return sample_dict
        except Exception as e:
            print(f"ERROR could not rank samples: {e}")
            return {}

#store = Audio_Recogniser()