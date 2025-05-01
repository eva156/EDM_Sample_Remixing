from pydub import AudioSegment
import numpy as np
import os

class Repeater:
    """
    Overlay a sample repeatedly over a silent track
    of a given duration at specified offsets

    Attributes:
        sample  : pydub AudioSegment containing single sample
        offsets : 1D array of times in seconds at which to play the sample
        track_duration : total length of output in seconds
    """
    def __init__(self, sample, offsets, track_duration):
        self.sample = sample
        self.offsets = np.sort(np.unique(offsets))
        self.track_duration = track_duration
    
    def sample_repeat(self):
        """
        render and return new AudioSegment of length track_duration
        with self.sample overlaid at each offset

        Returns:
            AudioSegment: the repeated sample track
        """
        len_ms = int(self.track_duration*1000)
        sound = AudioSegment.silent(duration=len_ms)
        for off in self.offsets:
            pos_ms = int(off * 1000)
            if 0 <= pos_ms < len_ms:
                sound = sound.overlay(self.sample, position=pos_ms)
        return sound[:len_ms]
    
    def export(self, path, format = "wav"):
        """
        render and write repeated track to destination
        
        Args:
            path : destination filepath
            format : audio format
        """
        repeated = self.sample_repeat()
        repeated.export(path, format=format)