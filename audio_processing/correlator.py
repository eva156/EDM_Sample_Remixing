import numpy as np
import scipy.signal
from typing import Tuple, Optional

class Correlator:
    """
    all similarity based analysis between a sample and the track

    Args:
        track_signal : 1D numpy array of full track waveform
        sr : sample rate of both track and samples
        track_max_time: duration (s) of the track
        downbeats : optional array of downbeat times
    """
    def __init__(self, track_signal, sr, track_max_time, downbeats=None):
        self.track_signal = track_signal
        self.sr = sr
        self.track_max_time = track_max_time
        self.downbeats = downbeats

    def full_correlation(self, sample_signal, lp_cutoff = 35.0, lp_order = 15):
        """
        computes normalised cross-correlation (FFT) between the track and a sample
        then apply low-pass filter to smooth it

        Returns:
            times : array of times in seconds
            corr : filtered, normalised correlation values
        """
        c = scipy.signal.correlate(self.track_signal, sample_signal, mode='valid', method='fft')
        c /= np.sqrt(np.sum(np.abs(sample_signal)**2)*np.sum(np.abs(self.track_signal)**2))
        sos = scipy.signal.butter(lp_order, lp_cutoff, 'lp', fs=1000, output='sos') 
        filtered = scipy.signal.sosfiltfilt(sos, c) 
        offsets = np.arange(0, len(c), 1)/self.sr
        self.last_full_calc = (offsets, filtered)
        return offsets, filtered
    
    def get_correlation_histogram(self, offsets, binwidth = 0.1):
        """
        Build a histogram of manually-detected match offsets

        Args:
            offsets : array of offsets
            binwidth : width of each time bin
        
        Returns:
            bins : left-edges of bins
            counts : counts per bin
        """

        if len(offsets) > 0:
            hist, bins = np.histogram(offsets,
                                bins=np.arange(0,
                                                int(self.track_max_time + binwidth + 1),
                                                binwidth))
            bins = bins[:-1]
            return (bins, hist)
        return ([],[])
    
    def downsample_corr(self, time, probs, factor=1000):
        """
        block-aggregate correlation curve by fixed factor

        Args:
            times : original time axis
            corr : original correlation values
            factor : downsampling factor
        Returns:
            new_times, new_corr where len(new_corr) = len(corr)//factor 
        """
        N = factor
        L = len(probs) // N
        probs_trim = probs[:L*N]
        time_trim = time[:L*N]
        probs_blockmax = probs_trim.reshape(L,N).max(axis=1)
        time_blockmean = time_trim.reshape(L,N).mean(axis=1)
        return time_blockmean, probs_blockmax
    
    def threshold(self, times, prob, min_corr):
        """
        pick out all times where correlation exceeds min_corr

        Args:
            times : array of time points
            prob : array of correlation values
            min_corr : threshold
        Returns:
            offsets : times[corr >= min_corr]
            values : array of min corr
        """
        corr_above = np.where(prob >= min_corr, times, -1)
        corr_above = corr_above[corr_above > 0]
        offsets = np.unique(np.round(corr_above, 2))
        val_arr = np.repeat(min_corr, len(offsets))
        return offsets, val_arr

    def beat_aligned(self, downbeat_probs):
        """
        if downbeats was provided, sample correlation only at those beat times
        correlation at downbeats would have been calculated during loop extraction

        Returns:
            (beat_times, beat_corrs)
        """
        if self.downbeats is None:
            raise RuntimeError("No downbeats provided")
        time = np.arange(0, len(self.track_signal), 1)/self.sr
        probs = np.zeros(time.shape)
        probs[np.searchsorted(time, self.downbeats[:-1])] = downbeat_probs
        return time, np.array(probs)
    
    def beat_aligned_sonic(self, downbeat_probs, time):
        """
        Sonic Pi samples have different format of downbeat probabilities stored in database
        downbeat_probs[0] : times found where sample matched to track
        downbeat_probs[1] : probability with which that match occurs

        Returns:
            (beat_times, beat_corrs)
        """
        if self.downbeats is None:
            raise RuntimeError("No downbeats provided")
        n = len(self.track_signal)
        probs = np.zeros(n+1, dtype=float)
        probs[np.searchsorted(time, downbeat_probs[0][:-1])] = downbeat_probs[1]
        probs = probs[:-1]
        return (time, np.array(probs))