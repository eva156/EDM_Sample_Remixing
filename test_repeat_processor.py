import pytest
import numpy as np
import audio_processing.repeat_processor as repeat_processor

# Dummy segment to simulate pydub.AudioSegment
class DummySegment:
    def __init__(self, duration):
        # duration in milliseconds
        self.duration = duration
        self.overlays = []
        self.export_calls = []

    @classmethod
    def silent(cls, duration):
        return cls(duration)

    def overlay(self, sample, position):
        # record the overlay call
        self.overlays.append((sample, position))
        return self

    def __len__(self):
        return self.duration

    def __getitem__(self, key):  # slicing
        # return self for simplicity
        return self

    def export(self, path, format):
        self.export_calls.append((path, format))

@pytest.fixture(autouse=True)
def patch_audio_segment(monkeypatch):
    # Replace AudioSegment in module under test
    monkeypatch.setattr(repeat_processor, 'AudioSegment', DummySegment)
    yield


def test_sample_repeat_no_offsets_returns_silent():
    # No offsets: expect a silent track of full duration
    rep = repeat_processor.Repeater(sample=DummySegment(100), offsets=[], track_duration=0.5)
    out = rep.sample_repeat()
    # Duration should be track_duration * 1000 ms
    assert isinstance(out, DummySegment)
    assert len(out) == 500
    # No overlays recorded
    assert out.overlays == []


def test_sample_repeat_single_offset_within_range():
    sample = DummySegment(200)
    # offset at 0.1s within 0.5s duration
    rep = repeat_processor.Repeater(sample=sample, offsets=[0.1], track_duration=0.5)
    out = rep.sample_repeat()
    # One overlay at position 100 ms
    assert len(out.overlays) == 1
    overlay_sample, pos = out.overlays[0]
    assert overlay_sample is sample
    assert pos == 100
    # Duration unchanged
    assert len(out) == 500


def test_sample_repeat_multiple_offsets_sorted_unique():
    sample = DummySegment(50)
    # unsorted with duplicates
    offsets = [0.3, 0.1, 0.3, 0.0]
    rep = repeat_processor.Repeater(sample=sample, offsets=offsets, track_duration=0.5)
    # Internally offsets should be sorted unique: [0.0,0.1,0.3]
    assert np.allclose(rep.offsets, [0.0, 0.1, 0.3])
    out = rep.sample_repeat()
    # All valid offsets produce overlays
    positions = [pos for _, pos in out.overlays]
    assert set(positions) == {0, 100, 300}


def test_sample_repeat_offsets_outside_range_ignored():
    sample = DummySegment(100)
    # offsets negative and beyond track duration
    offsets = [-0.1, 0.0, 1.0]
    rep = repeat_processor.Repeater(sample=sample, offsets=offsets, track_duration=0.5)
    out = rep.sample_repeat()
    # Only offset 0.0 is valid
    assert len(out.overlays) == 1
    assert out.overlays[0][1] == 0


def test_export_writes_file(tmp_path, monkeypatch):
    # Monkeypatch sample_repeat to return dummy
    dummy = DummySegment(250)
    monkeypatch.setattr(repeat_processor.Repeater, 'sample_repeat', lambda self: dummy)
    rep = repeat_processor.Repeater(sample=dummy, offsets=[0], track_duration=0.25)
    out_path = tmp_path / "out.wav"
    rep.export(str(out_path), format="wav")
    # Verify export was called with correct args
    assert dummy.export_calls == [(str(out_path), 'wav')]

if __name__ == "__main__":
    import sys
    errno = pytest.main([__file__])
    sys.exit(errno)