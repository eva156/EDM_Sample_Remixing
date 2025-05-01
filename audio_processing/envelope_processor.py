from dataclasses import dataclass
from pydub import AudioSegment
import math
from typing import List
import numpy as np

@dataclass
class EnvelopePoint:
    """A single point in an ADSR envelope"""
    time: float # seconds from start
    level: float # absolute amplitude: 0.0-1.0 of max vol

@dataclass
class Envelope:
    """All points of ADSR envelope"""
    start: EnvelopePoint
    attack: EnvelopePoint
    decay: EnvelopePoint
    sustain: EnvelopePoint
    release: EnvelopePoint

class EnvelopeProcessor:
    """
    Apply ADSR envelop to a pydub AudioSegment

    - convert level -> dB for pydub fades
    - slice the source audio into segments
    - insert leading/trailing silence if needed
    - apply fade-in/out between each pair of envelope points
    - return new AudioSegment with envelope applied
    """
    def __init__(self, sound):
        self.sound = sound
        self.max_vol = sound.max
    
    def _level_to_db(self, level):
        """
        convert amplitude level to relative dB 
        zero maps to very low floor
        Args:
            level : either 0.0-1.0 fraction or absolute amplitude
        """
        if level > 1:
            rel = level / self.max_vol
        else:
            rel = level
        if level == 0:
            dB = -120
        else:
            dB = np.round(20*np.log10(rel),3)
        return dB
            

    def implement_envelope(self, env):
        """
        apply ADSR envelope to sound

        Args:
            env: envelope with absolute times (secs) and levels (0-1)

        Returns:
            new AudioSegment with envelope applied
        """
        #new_sound = AudioSegment.silent(duration=int(env.start.time*1000))
        chunks = [] 
        silent_start = AudioSegment.silent(duration=int(1000*env.start.time))
        chunks.append(silent_start)
        
        env_points = [env.start, env.attack, env.decay, env.sustain, env.release]
        for p1, p2 in zip(env_points, env_points[1:]):
            chunk = self.sound[int(1000*p1.time): int(1000*p2.time)]
            dB1 = self._level_to_db(p1.level)
            dB2 = self._level_to_db(p2.level)
            if p1.time != p2.time and len(chunk) > 0:
                chunk = chunk.fade(to_gain=dB2, from_gain=dB1, start=0, end=len(chunk))
            chunks.append(chunk)
        end_ms = env_points[-1].time*1000
        if end_ms < len(self.sound):
            silent_end = AudioSegment.silent(duration=len(self.sound)-int(end_ms))
            chunks.append(silent_end)
        new_sound = sum(chunks)
        return new_sound