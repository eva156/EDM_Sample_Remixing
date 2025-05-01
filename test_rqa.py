import pytest
import numpy as np
import synthesis.rqa_detector as rqa_detector


# Dummy classes to stub heavy dependencies
class DummyResult:
    # 16 features in order used by RQA_Detector
    fields = [
        'recurrence_rate', 'determinism', 'average_diagonal_line', 'longest_diagonal_line',
        'divergence', 'entropy_diagonal_lines', 'laminarity', 'trapping_time',
        'longest_vertical_line', 'entropy_vertical_lines', 'average_white_vertical_line',
        'longest_white_vertical_line', 'longest_white_vertical_line_inverse',
        'entropy_white_vertical_lines', 'ratio_determinism_recurrence_rate',
        'ratio_laminarity_determinism'
    ]
    def __init__(self, val=1.0):
        for name in self.fields:
            setattr(self, name, val)

class DummyComputation:
    def __init__(self, settings):
        pass
    def run(self):
        return DummyResult(val=2.0)

class DummyPelt:
    def __init__(self, model):
        self.model = model
        self.features = None
    def fit(self, features):
        # Store features for predict
        self.features = features
        return self
    def predict(self, *args, **kwargs):
        # Return a list including last index to test removal
        # Use stored features length
        if self.features is None:
            return []
        return [len(self.features)]

class DummyVMM:
    def __init__(self, max_order=0):
        self.max_order = max_order
        self.calls = []
    def vmm(self, binary_encoding, cluster_patterns, segments, window_labels, window_pos, change_points, beat_classes, occurrence_weight):
        # Echo back inputs for assertion
        return {
            'encoding': binary_encoding,
            'patterns': cluster_patterns,
            'segments': segments,
            'labels': window_labels,
            'windows': window_pos,
            'changes': change_points,
            'beat_classes': beat_classes,
            'weight': occurrence_weight
        }

@pytest.fixture(autouse=True)
def patch_dependencies(monkeypatch):
    # Stub pyrqa and ruptures dependencies
    monkeypatch.setattr(rqa_detector, 'RQAComputation', type('RC', (), {'create': staticmethod(lambda settings: DummyComputation(settings))}))
    monkeypatch.setattr(rqa_detector, 'TimeSeries', lambda window, embedding_dimension, time_delay: None)
    monkeypatch.setattr(rqa_detector, 'Settings', lambda **kwargs: None)
    monkeypatch.setattr(rqa_detector, 'FixedRadius', lambda radius: None)
    monkeypatch.setattr(rqa_detector, 'EuclideanMetric', None)
    monkeypatch.setattr(rqa_detector.rpt, 'Pelt', DummyPelt)
    monkeypatch.setattr(rqa_detector, 'VMM', DummyVMM)
    yield


def test_recurrence_quantification_analysis_padding():
    rd = rqa_detector.RQA_Detector()
    # Input shorter than window_size (16)
    data = [1, 0, 1]
    padded, features, window_pos = rd.recurrence_quantification_analysis(data)
    # data padded to length 16
    assert len(padded) == 16
    # Only one window: (16-16)/4 + 1
    assert features.shape == (1, 16)
    # Window position starts at 0
    assert window_pos == [0]
    # All features normalized to zero (since single window mean=val and std=0 -> zero after nan_to_num)
    assert np.allclose(features, np.zeros_like(features))


def test_point_change_analysis_single_window():
    rd = rqa_detector.RQA_Detector()
    data = np.array([0, 1, 0, 1, 0])
    # One window
    rqa_features = np.zeros((1, 16))
    window_pos = [0]
    class_patterns, segments, labels, wpos, changes, beat_classes = rd.point_change_analysis('test', data, rqa_features, window_pos)
    # No change points
    assert changes == []
    # Single label 0
    assert labels.tolist() == [0]
    # All beat_classes zero
    assert beat_classes.tolist() == [0] * len(data)
    # segments and class_patterns contain full data
    assert isinstance(class_patterns, dict) and 0 in class_patterns
    assert np.array_equal(class_patterns[0], data)
    assert len(segments) == 1


def test_point_change_analysis_multiple_windows():
    rd = rqa_detector.RQA_Detector()
    # Create synthetic data and two windows
    data = np.arange(20)
    rqa_features = np.zeros((2, 16))
    window_pos = [0, 4]
    class_patterns, segments, labels, wpos, changes, beat_classes = rd.point_change_analysis('test', data, rqa_features, window_pos)
    # DummyPelt.predict returns [2] which is removed, so no change points
    assert changes == []
    # Two windows => two labels
    assert labels.tolist() == [0, 0]
    # beat_classes length == data length
    assert len(beat_classes) == len(data)
    # segments correspond to full data
    assert len(segments) == 1 and np.array_equal(segments[0], data)


def test_sample_pattern_detection_and_sonic(monkeypatch):
    rd = rqa_detector.RQA_Detector()
    # Dummy sample
    class Sample:
        def __init__(self):
            self.offsets = np.array([0, 2])
            self.name = 'foo.wav'
    sample = Sample()
    downbeats = [0, 1, 2]
    # Patch internal methods
    monkeypatch.setattr(rqa_detector.RQA_Detector, 'recurrence_quantification_analysis', lambda self, data, name: (data, 'feat', 'wpos'))
    monkeypatch.setattr(rqa_detector.RQA_Detector, 'point_change_analysis', lambda self, name, data, feat, wpos: ('patterns', 'segments', 'labels', 'wpos', 'changes', 'beats'))
    # Test sample_pattern_detection
    out = rd.sample_pattern_detection(sample, downbeats)
    # Expected binary encoding: [1,0,1]
    assert isinstance(out, dict)
    assert out['encoding'] == [1, 0, 1]
    assert out['patterns'] == 'patterns'
    assert out['weight'] == 1
    # Test sonic_sample_pattern_detection
    beats = [0.0, 1.0]
    sample.offsets = np.array([0.1])
    out2 = rd.sonic_sample_pattern_detection(sample, beats)
    # encoding length matches beats, occurrence_weight = 2*len(beats)
    assert out2['encoding'] and out2['weight'] == 2 * len(beats)


if __name__ == "__main__":
    import sys
    errno = pytest.main([__file__])
    sys.exit(errno)