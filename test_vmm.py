import pytest
import numpy as np
from synthesis.variable_markov_model import VMM


class SimpleVMM(VMM):
    """Subclass to override get_probability_distribution for deterministic tests."""
    def get_probability_distribution(self, counts, context):
        # Always predict 100% for bit=1
        return np.array([0.0, 1.0])

def test_build_vmm_model_simple():
    # simple sequence [1,0], max_order=1, occurrence_weight=0
    seq = [1, 0]
    vmm = VMM(max_order=1)
    counts = vmm.build_vmm_model([seq], occurence_weight=0, max_order=1)
    # Context before second bit: context=(1,) -> next_state=0, weight=10
    assert counts[(1,)][0] == 16
    # No unexpected contexts
    assert set(counts.keys()) == {(1,)}

@pytest.mark.parametrize("counts,context,expected", [
    ({('a',): np.array([2, 2])}, ('a',), np.array([0.5, 0.5])),
    ({('x', 'y'): np.array([1, 3])}, ('x','y'), np.array([0.25, 0.75])),
])
def test_get_probability_distribution_exact(counts, context, expected):
    vmm = VMM()
    pdist = vmm.get_probability_distribution(counts, context)
    assert np.allclose(pdist, expected)

def test_get_probability_distribution_backoff_and_zero():
    vmm = VMM()
    # counts empty or zero-sum should return zeros
    counts = {('a',): np.array([0.0, 0.0])}
    pdist = vmm.get_probability_distribution(counts, ('a',))
    assert np.allclose(pdist, [0.5, 0.5])
    pdist2 = vmm.get_probability_distribution({}, ('b',))
    assert np.allclose(pdist2, [0.5, 0.5])

def test_vmm_sequence_viterbi_all_ones():
    # With overridden get_probability_distribution always returning [0,1]
    iv_counts = {}  # unused for SimpleVMM
    vmm = SimpleVMM(max_order=1)
    seq = vmm.vmm_sequence_viterbi(iv_counts, max_order=1, target_length=5)
    # Expect sequence of length 5: five 1s
    assert isinstance(seq, list)
    assert len(seq) == 5
    assert seq == [1,1,1,1,1]

def test_vmm_full_pipeline(monkeypatch):
    # Stub build_vmm_model and vmm_sequence_viterbi
    patterns = {0: [0,1,0,1], 1: [1,1,0,1,0]}
    vmm = VMM()
    calls = []
    def fake_build(seqs, weight, max_order=8):
        calls.append(('build', seqs, weight))
        return 'cnts', 'initial'
    def fake_decode(cnts, mo, length):
        calls.append(('decode', cnts, length))
        return ['decoded']
    monkeypatch.setattr(vmm, 'build_vmm_model', fake_build)
    monkeypatch.setattr(vmm, 'vmm_sequence_viterbi', fake_decode)
    # Test with binary_encoding and window data
    bin_enc = [0,1,0,1,1,1,0,1,0]
    window_labels = [0,1]
    window_pos = [0,4]
    detected = vmm.vmm(bin_enc, patterns, segments=None, window_labels=window_labels, window_pos=window_pos, change_points=None, beat_classes=None)
    # Should call build and decode for each cluster label
    assert calls[0][0] == 'build'
    assert calls[1][0] == 'decode'
    assert isinstance(detected, list) and detected == [['decoded'], ['decoded']]

if __name__ == "__main__":
    import sys
    errno = pytest.main([__file__])
    sys.exit(errno)