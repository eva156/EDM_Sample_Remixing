import pytest
import numpy as np
import audio_processing.envelope_processor as envelope_processor


class DummySegment:
    fade_calls = []

    def __init__(self, duration, max=1000):
        self.duration = duration
        self.max = max
    
    def __len__(self):
        return self.duration

    def __getitem__(self, key):
        # key is slice indices - start, end 
        start = key.start
        end = key.stop
        start = max(0, int(start))
        clipped_end = min(int(end), self.duration)
        length = max(0, clipped_end - start)
        return DummySegment(length, self.max)
    
    def fade(self, to_gain, from_gain, start, end):
        DummySegment.fade_calls.append((from_gain, to_gain, start, end))
        return self
    
    @staticmethod
    def silent(duration):
        return DummySegment(int(duration), max=0)
    
    def __add__(self, other):
        if isinstance(other, DummySegment):
            return DummySegment(self.duration + other.duration, max=self.max)
        return NotImplemented

    def __radd__(self, other):
        if other == 0:
            return self
        return self.__add__(other)
    
@pytest.fixture(autouse=True)
def path_audio_segment(monkeypatch):
    # replace AudioSegment in envelope_processor with DummySegment
    monkeypatch.setattr(envelope_processor, 'AudioSegment', DummySegment)
    yield
    # clear fade_calls after each test
    DummySegment.fade_calls.clear()

@ pytest.mark.parametrize("level, max_vol, expected_dB", [
    (0, 1000, -120),
    (0.5, 1000, pytest.approx(-6.021, abs=1e-3)),
    (1.0, 1000, 0.0),
    (2.0, 2.0, 0.0),
])
def test_level_to_db(level, max_vol, expected_dB):
    dummy = DummySegment(100, max=max_vol)
    proc = envelope_processor.EnvelopeProcessor(dummy)
    dB = proc._level_to_db(level)
    assert dB == expected_dB

def test_implement_envelope_with_silent_end():
    # sound longer than realease time then silent end appended
    sound = DummySegment(1000)
    proc = envelope_processor.EnvelopeProcessor(sound)
    env = envelope_processor.Envelope(
        start=envelope_processor.EnvelopePoint(0.0, 0.0),
        attack=envelope_processor.EnvelopePoint(0.1, 1.0),
        decay=envelope_processor.EnvelopePoint(0.2, 0.5),
        sustain=envelope_processor.EnvelopePoint(0.3, 0.5),
        release=envelope_processor.EnvelopePoint(0.4, 0.0),
    )
    out = proc.implement_envelope(env)
    assert isinstance(out, DummySegment)
    assert len(out) == len(sound)

def test_implement_envelope_no_silent_end_when_release_at_end():
    # Release time equals sound length => no silent_end
    sound = DummySegment(1000)
    proc = envelope_processor.EnvelopeProcessor(sound)
    env = envelope_processor.Envelope(
        start=envelope_processor.EnvelopePoint(0.0, 0.0),
        attack=envelope_processor.EnvelopePoint(0.25, 1.0),
        decay=envelope_processor.EnvelopePoint(0.50, 0.5),
        sustain=envelope_processor.EnvelopePoint(0.75, 0.5),
        release=envelope_processor.EnvelopePoint(1.0, 0.0),
    )
    out = proc.implement_envelope(env)
    # Durations: chunks sum to 1000ms, no silent_end
    assert len(out) == 1000


def test_implement_envelope_fade_calls_for_nonzero_slices():
    # Envelope with last two points at same time => one zero-length slice
    sound = DummySegment(400)
    proc = envelope_processor.EnvelopeProcessor(sound)
    env = envelope_processor.Envelope(
        start=envelope_processor.EnvelopePoint(0.0, 0.0),
        attack=envelope_processor.EnvelopePoint(0.1, 1.0),
        decay=envelope_processor.EnvelopePoint(0.2, 0.5),
        sustain=envelope_processor.EnvelopePoint(0.3, 0.5),
        release=envelope_processor.EnvelopePoint(0.3, 0.0),
    )
    out = proc.implement_envelope(env)
    # There are four p1->p2 pairs; one is zero-length, so only 3 fades
    assert len(DummySegment.fade_calls) == 3
    # Check that fade calls have correct from_gain and to_gain ordering
    from_gains = [call[0] for call in DummySegment.fade_calls]
    to_gains = [call[1] for call in DummySegment.fade_calls]
    # First fade: level 0.0->1.0 => dB -120->0
    assert from_gains[0] == proc._level_to_db(0.0)
    assert to_gains[0]   == proc._level_to_db(1.0)


if __name__ == "__main__":
    import sys
    errno = pytest.main([__file__])
    sys.exit(errno)