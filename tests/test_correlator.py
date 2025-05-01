import pytest
import numpy as np
from audio_processing.correlator import Correlator


@ pytest.fixture(autouse=True)
def patch_lowpass(monkeypatch):
    """
    Stub the low-pass filter to identity for full_correlation tests.
    """
    import audio_processing.correlator as correlator
    monkeypatch.setattr(correlator.scipy.signal, 'butter', lambda *args, **kwargs: None)
    monkeypatch.setattr(correlator.scipy.signal, 'sosfiltfilt', lambda sos, data: data)
    yield


def test_full_correlation_simple():
    # Simple track and sample signals
    track = np.array([1, 2, 3], dtype=float)
    sample = np.array([1, 0], dtype=float)
    # sr=1 for easy offset calculation, track_max_time unused here
    corr = Correlator(track_signal=track, sr=1, track_max_time=3)
    times, values = corr.full_correlation(sample_signal=sample)
    # Manual correlation: [1, 2] normalized by sqrt(1 * 14)
    expected = np.array([1, 2]) / np.sqrt(np.sum(track**2) * np.sum(sample**2))
    assert np.allclose(times, np.array([0, 1]))
    assert np.allclose(values, expected)
    # last_full_calc should store the same arrays
    assert corr.last_full_calc[0] is times
    assert corr.last_full_calc[1] is values


def test_get_correlation_histogram_empty():
    corr = Correlator(track_signal=np.zeros(10), sr=1, track_max_time=5)
    bins, counts = corr.get_correlation_histogram(np.array([]))
    assert bins == [] and counts == []


def test_get_correlation_histogram_counts():
    offsets = np.array([0.1, 0.2, 1.5, 2.5])
    corr = Correlator(track_signal=np.zeros(100), sr=1, track_max_time=3)
    bins, counts = corr.get_correlation_histogram(offsets, binwidth=1.0)
    # Bins: [0,1,2,3]; Counts: 2 in [0-1], 1 in [1-2], 1 in [2-3]
    assert np.allclose(bins, np.array([0, 1, 2, 3]))
    assert np.array_equal(counts, np.array([2, 1, 1, 0]))


def test_downsample_corr():
    time = np.arange(6, dtype=float)
    probs = np.arange(6, dtype=float)
    corr = Correlator(track_signal=np.zeros(6), sr=1, track_max_time=6)
    t2, p2 = corr.downsample_corr(time, probs, factor=2)
    # Expect 3 blocks: times [0.5,2.5,4.5], max vals [1,3,5]
    assert np.allclose(t2, np.array([0.5, 2.5, 4.5]))
    assert np.allclose(p2, np.array([1, 3, 5]))


def test_threshold():
    times = np.array([0.1, 0.2, 0.3, 0.4])
    vals = np.array([0.5, 0.8, 0.2, 0.9])
    corr = Correlator(track_signal=np.zeros(4), sr=1, track_max_time=4)
    offsets, mins = corr.threshold(times, vals, min_corr=0.75)
    # Should pick times 0.2 and 0.4
    assert np.allclose(offsets, np.array([0.2, 0.4]))
    assert np.allclose(mins, np.array([0.75, 0.75]))


def test_beat_aligned_requires_downbeats():
    corr = Correlator(track_signal=np.zeros(10), sr=1, track_max_time=10)
    with pytest.raises(RuntimeError):
        corr.beat_aligned(np.array([0.5, 0.6]))


def test_beat_aligned():
    # Provide downbeats and corresponding probabilities
    downbeats = np.array([0.0, 2.0, 4.0])
    probs = np.array([0.7, 0.8])
    corr = Correlator(track_signal=np.zeros(5), sr=1, track_max_time=5, downbeats=downbeats)
    time, beat_corr = corr.beat_aligned(probs)
    # Time axis 0,1,2,3,4
    assert np.allclose(time, np.arange(5))
    # Prob at indices 0 and 2
    expected = np.zeros(5)
    expected[0] = 0.7
    expected[2] = 0.8
    assert np.allclose(beat_corr, expected)


def test_beat_aligned_sonic_requires_downbeats():
    corr = Correlator(track_signal=np.zeros(4), sr=1, track_max_time=4)
    with pytest.raises(RuntimeError):
        corr.beat_aligned_sonic((np.array([0.0]), np.array([0.5])), np.arange(4))


def test_beat_aligned_sonic():
    track = np.zeros(4)
    downbeats = np.array([0.0, 2.0])
    # times where sample matched (include dummy last point)
    match_times = np.array([0.0, 2.0])
    match_probs = np.array([0.5])
    corr = Correlator(track_signal=track, sr=1, track_max_time=4, downbeats=downbeats)
    time = np.arange(4)
    t_out, p_out = corr.beat_aligned_sonic((match_times, match_probs), time)
    # Should assign 0.5 at index corresponding to time 0.0 (0)
    assert np.allclose(t_out, time)
    expected = np.zeros_like(time, dtype=float)
    expected[0] = 0.5
    assert np.allclose(p_out, expected)

if __name__ == "__main__":
    import sys
    errno = pytest.main([__file__])
    sys.exit(errno)