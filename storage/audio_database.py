import numpy as np
from pymongo import MongoClient
#from scipy.io.wavfile import read, write
import os
import gridfs

"""
simple GridFS MongoDB wrapper for storing and retrieving
audio files and their metadata, specialised for extracted
samples and Sonic Pi sample collections
"""

class Database:
    """
    Base wrapper around MongoDB GridFS bucket for binary files
    
    Attributes:
        db  (Database): The PyMongo database instance
        bucket  (GridFS):   The GridFS bucket for file storag
    """
    def __init__(self, name):
        """
        Connect to localhost and open or create database called 'name
        """
        self.cluster = MongoClient("localhost", 27017)
        #database
        self.db = self.cluster[name]
        self.bucket = gridfs.GridFS(self.db)
    
    def add_one_audio_file(self, url, name):
        """
        Store the file at 'url' in GridFS under key 'name'

        Args:
            url:    Path on local filesystem
            name:   Filename to assign in GridFS
        """
        with open(url, "rb") as file_data:
            file_id = self.bucket.put(file_data, filename=name)
    
    def read_one_audio_file_name(self, name, dest, temp=False):
        """
        Export content of audio file to dest, identifying the file by its name
        
        Args:
            name:   Name of file in database
            dest:   Path to store file contents to
            temp:   Bool indicating if file is temporary
        """
        results = self.bucket._files.find_one({'filename': name})
        if results:
            if temp:
                dest.write(self.bucket.get(results['_id']).read())
            else:
                with open(dest, 'wb') as output_file:
                    output_file.write(self.bucket.get(results['_id']).read())
        else:
            print("file not found", name)

    def read_one_audio_file_id(self, id, dest, temp=False):
        """
        Write content of file to dest, identifying the file by its file ID
        
        Args:
            name:   File ID of file in database
            dest:   Path to store file contents to
            temp:   Bool indicating if file is temporary
        """
        results = self.bucket._files.find_one({'_id': id})
        if results:
            if temp:
                dest.write(self.bucket.get(results['_id']).read())
            else:
                with open(dest, 'wb') as output_file:
                    output_file.write(self.bucket.get(results['_id']).read())
        else:
            print("file not found", id)
    
    def file_exists(self, name):
        """
        Check if 'name' is in GridFS

        Returns:
            file ID or False
        """
        result = self.bucket._files.find_one({'filename': name})
        if result:
            return result['_id']
        return False

class SonicPiSampleDatabase(Database):
    """
    Stores and retrieves Sonic Pi samples from dedicated database

    Inherits from Database and uses local 'sample-pi-main' folder for bulk upload
    """
    def __init__(self):
        super().__init__("SonicPiSamples")
        self.folder = "C:/Users/uno4e/OneDrive/Documents/Cambridge II/project/sample-pi-main"
    
    def add_sonic_samples(self):
        """
        Upload any wav files not already in GridFS
        """
        for i, name in enumerate(os.listdir(self.folder)):
            path = os.path.join(self.folder, name)
            if os.path.isfile(path):
                self.add_one_audio_file(path, name)
    
    def get_sonic_names(self):
        """
        Returns:
            names:  all sample names stored to GridFS
        """
        names = []
        for f in self.bucket._files:
            names.append(f['filename'])
        return names


class ProjectDatabase(Database):
    """
    Stores and retrieves files for a single project
    """
    def __init__(self, name):
        super().__init__(name)
    
    def add_full_track_file(self, path, downbeats):
        """
        Read local file and store it as the original full track for the project
        Stores downbeats as metadata
        
        Args:
            path:   local path to file
            downbeats:  timings in track of detected downbeats

        Returns:
            fileID or None if upload failed
        """

        # each project can only have one full_track
        # if one is already stored delete it
        result = self.bucket._files.find_one({'filename': 'full_track'})
        if result:
            self.bucket.delete(result['_id'])
        
        try:
            with open(path, "rb") as file_data:
                file_id = self.bucket.put(file_data, filename='full_track', metadata={"downbeats": downbeats})
        except Exception as e:
            print("Failed to save original track to database:", e)
            return None
        return file_id
    
    def add_one_sample_file_with_env_list(self, name, path, env, min_corr, bar_probs, rank):
        """
        env: coordinates for samples envelope in form [[xs], [ys]]
        """
        start = (env[0][0], env[1][0])
        attack = (env[0][1], env[1][1])
        decay = (env[0][2], env[1][2])
        sustain = (env[0][3], env[1][3])
        release = (env[0][4], env[1][4])
        return self.add_one_sample_file(name, path, start, attack, decay, sustain, release, min_corr, bar_probs, rank)
    
    def add_one_sample_file(self, name, path, start, attack, decay, sustain, release, min_corr, bar_probs, rank, buf=False):
        """
        Read local file and store it as a sample
        Stores envelope, min correlation, downbeat probababilities, rank as metadata
        
        Args:
            path:   local path to file
            start, attack, decay, sustain, release: coordinates for samples envelope
            min_corr:   minimum similarity required for sample instance to be included
            bar_probs:  probability of sample occurring at each downbeat
            rank:   for Sonic Pi samples provide rank of how similar sample is to track
            buf:    boolean indicating if the path is actually raw audio data in a buffer

        Returns:
            fileID or None if upload failed or sample of same name already stored
        """
        
        result = self.bucket._files.find_one({'filename': name})
        if result:
            return None
        else:
            try:
                if buf:
                    file_id = self.bucket.put(path.read(), filename=name, metadata={"start": start, "attack": attack, "decay": decay, "sustain": sustain, "release": release, "min_corr": min_corr, "bar_probs": bar_probs, "rank":rank})
                else:
                    with open(path, "rb") as file_data:
                        file_id = self.bucket.put(file_data, filename=name, metadata={"start": start, "attack": attack, "decay": decay, "sustain": sustain, "release": release, "min_corr": min_corr, "bar_probs": bar_probs, "rank":rank})
                return file_id
            except Exception as e:
                print("Failed to store sample file:", e)
                return None
        
    def add_repeat_sample_file(self, name, path):
        """
        Read local file and store it as a track of how a sample repeas throughout the track
        Stores downbeats as metadata
        
        Args:
            name:   name to sure file under
            path:   local path to file
        Returns:
            fileID or None if upload failed
        """
        result = self.bucket._files.find_one({'filename': name})
        if result:
            self.bucket.delete(result['_id'])
        try:
            with open(path, "rb") as file_data:
                file_id = self.bucket.put(file_data, filename=name)
        except Exception as e:
            print("Failed to store repeated sample file to database:", e)
            return None
        return file_id

    def add_source_separated_loop(self, name, buf):
        """
        Read buffer with audio data and store it as a track 
        of how a sample repeas throughout the track
        Stores downbeats as metadata
        
        Args:
            name:   name to sure file under
            buf:    buffer with audio data   
        Returns:
            fileID or None if upload failed or sample of same name already stored
        """
        result = self.bucket._files.find_one({'filename': name})
        if result:
            self.bucket.delete(result['_id'])
        try:
            file_id = self.bucket.put(buf.read(), filename=name)
        except Exception as e:
            print("Failed to store repeated sample file to database:", e)
            return None
        return file_id

    def get_envelope(self, name):
        """
        Get the envelope of sample file 'name'

        Args:
            name: GridFS filename to look up
        
        Returns:
            envelope in form [x coordinates, y coordinates]
            None if no file found
        """
        result = self.bucket._files.find_one({'filename': name})
        if result:
            start = result['metadata']["start"]
            attack = result['metadata']["attack"]
            decay = result['metadata']["decay"]
            sustain = result['metadata']["sustain"]
            release = result['metadata']["release"]
            return ([start[0], attack[0], decay[0], sustain[0], release[0]], [start[1], attack[1], decay[1], sustain[1], release[1]])
        else:
            return None
    
    def get_min_corr(self, name):
        """
        Get the min correlation of sample file 'name'

        Args:
            name: GridFS filename to look up
        
        Returns:
            min correlation
            None if no file found
        """
        result = self.bucket._files.find_one({'filename': name})
        if result:
            return result['metadata']["min_corr"]
        return None
    
    def get_bar_probs(self, name):
        """
        Get the occurence probabilities of sample file 'name'

        Args:
            name: GridFS filename to look up
        
        Returns:
            probabilities
            None if no file found
        """
        result = self.bucket._files.find_one({'filename': name})
        if result:
            return result['metadata']["bar_probs"]
        return None
    
    def get_downbeats(self):
        """
        Get the downbeats of full track file

        Returns:
            list of downbeats
            empty list if no file found
        """
        result = self.bucket._files.find_one({'filename':'full_track'})
        #print(result)
        if result:
            return result['metadata']['downbeats']
        return []

    def update_sample_data(self, sample):
        """
        Replace sample file with updated information

        Args:
            sample: instance of SampleFile class (from audiofile_manager)
        """
        result = self.bucket._files.find_one({'filename': sample.name})
        if result:
            self.bucket.delete(result['_id'])
        new = self.add_one_sample_file_with_env_list(sample.name, sample.file_path, sample.get_envelope(), sample.min_corr, list(sample.downbeat_probs), 0)
    
    def get_separated_loop_tracks(self, dest):
        """
        Find and write source separated loops of original file to dest

        Args:
            dest:   path to write files to
        Returns:
            list of file paths
        """
        result = self.bucket._files.find({"filename": "separated_loop.wav"})
        files = []
        for i, r in enumerate(result):
            self.read_one_audio_file_id(r['_id'], f"{dest}/separated_track{i}.wav")
            files.append(f"{dest}/separated_track{i}.wav")
        return files

    def get_sample_names(self):
        """
        Get list of extracted samples saved in project database

        Returns:
            list of sample names
        """
        samples = []
        names = self.bucket.list()
        for n in names:
            result = self.bucket._files.find_one({"filename": n})
            if result:
                if result.get('metadata') != None:
                    #print(result['metadata'])
                    #rank = result['metadata'].get('rank')
                    occurrence_probs = result['metadata'].get('bar_probs')
                    # if it is a sample file it will have a rank in its metadata
                    # if it is an extracted sample occurrence probailities will be a 1D list
                    if occurrence_probs != None:
                        if len(occurrence_probs) > 2:
                            samples.append(n)
        return samples
    
    def get_sonic_sample_names(self):
        """
        Get list of sonic pi samples saved in project database

        Returns:
            list of sample names
        """
        samples = []
        names = self.bucket.list()
        for n in names:
            result = self.bucket._files.find_one({"filename": n})
            if result:
                if result.get('metadata') != None:
                    rank = result['metadata'].get('rank')
                    # if it is a sample file it will have a rank in its metadata
                    # if it is a sonic pi sample the rank will be greater than 0
                    if rank != None and rank != 0:
                        samples.append(n)
        return samples
    
    def get_order_sonic_pi_samples(self):
        """
        Get the ranked order of sonic pi samples

        Returns:
            list of sonic pi samples ordered by rank
        """
        sample_names = self.get_sonic_sample_names()
        samples = []
        ranks = []
        for s in sample_names:
            result = self.bucket._files.find_one({"filename": s.upper()})
            if result:
                ranks.append(int(result['metadata']['rank']))
                samples.append(s.lower())
        ranks = np.array(ranks, dtype=np.int32)
        samples = np.array(samples)
        #print(ranks)
        order = np.argsort(ranks)
        samples = samples[order]
        return samples

#database = SonicPiSampleDatabase()
#database.read_one_audio_file("audio.wav")
#database.add_file()
#database.read_file()

"""
jWrEgPKboc4F77tz
"""