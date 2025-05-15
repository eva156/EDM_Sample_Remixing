import os
import numpy as np
import pytest


from synthesis.program_generator import (
    ProgramGenerator,
    LoopProgramGenerator,
    PloynomialProgramGenerator,
    DSLProgramGenerator
)
import synthesis.sonic_pi_dsl as dsl

# Helpers for dummy samples and env points
class EnvPoint:
    def __init__(self, time, level):
        self.time = time
        self.level = level

class DummySample:
    def __init__(self, name, offsets, max_time, max_vol=1.0):
        self.name = name
        self.offsets = np.array(offsets)
        self.max_time = max_time
        self.max_vol = max_vol
        self.original_vol = max_vol
        # create an env with predictable times and levels
        self.env = type('E', (), {
            'start': EnvPoint(0.1, 0.2),
            'attack': EnvPoint(0.3, 0.8),
            'decay': EnvPoint(0.5, 0.5),
            'sustain': EnvPoint(0.7, 0.5),
            'release': EnvPoint(1.0, 0.0)
        })
        # dummy correlation
        self.corr = (np.array([0.0, max_time]), np.array([1.0, 0.9]))
        self.file_path = f"/tmp/{name}.wav"
        self.checked = True
        # dummy full_track for DSL
        class FT: pass
        self.full_track = FT()
        self.full_track.downbeats = np.array([0.0, 0.5, 1.0])
        self.full_track.tempo = 120

@pytest.fixture
def tmp_dest(tmp_path, monkeypatch):
    # ensure directory exists
    dest = tmp_path / "outdir"
    dest.mkdir()
    return str(dest)


def test_calc_env_duration_and_level():
    pg = ProgramGenerator([], [])
    # duration: end - start
    assert pg.calc_env_duration(0.5, 1.2345) == pytest.approx(0.734, abs=1e-6)
    # level: (val2-val1)/max, rounded
    assert pg.calc_env_level(0.2, 0.8, 1.0) == pytest.approx(0.6)


def test_get_env():
    sample = DummySample('s1', offsets=[0.0], max_time=1.0, max_vol=2.0)
    pg = ProgramGenerator([sample], [])
    env_tuple = pg.get_env(sample)
    # expect 5 durations and 3 levels
    assert len(env_tuple) == 8
    # start duration: env.start.time
    assert env_tuple[0] == pytest.approx(0.1)
    # attack duration: 0.3-0.1
    assert env_tuple[1] == pytest.approx(0.2)
    # attack level: (0.8-0.2)/2.0
    assert env_tuple[5] == pytest.approx((0.8-0.2)/2.0, abs=1e-3)


def test_filter_offsets():
    lp = LoopProgramGenerator([], [])
    offsets = [0.0, 0.4, 0.9, 1.5]
    included, not_incl = lp.filter_offsets(offsets, sample_len=0.6)
    # first always included
    assert included[0] == 0.0
    # 0.4 dropped (0.4-0.0<0.6), next 0.9 included
    assert 0.9 in included and 0.4 in not_incl
    # 1.5 included because 1.5-0.9>=0.6
    assert 1.5 in included


def test_filter_offsets_structured():
    lp = LoopProgramGenerator([], [])
    offsets = [0.2, 0.5, 1.0]
    sleep_times, deferred = lp.filter_offsets_structured(offsets, sample_len=0.1)
    # structured includes [0, offset0] -> [0,0.2], sample_len=0.4: offset0 at 0.2
    # offset1=0.5-0.2>=0.4 => included
    # offset2=1.0-0.5>=0.4 => included
    assert isinstance(sleep_times, list) and isinstance(deferred, list)
    # sleep_times: diffs between [0,0.2,0.5,1.0]: [0.2,0.3,0.5]
    assert sleep_times == [pytest.approx(0.2), pytest.approx(0.3), pytest.approx(0.5)]
    assert deferred == []


def test_group_consecutive_beats():
    p = [1,1,0,1,1,1,0]
    pg = DSLProgramGenerator([], [])
    groups, starts = pg.group_consecutive_beats(p, target=1)
    assert groups == [2, 3]
    assert starts == [0, 3]


def test_modulus_groups_and_covered():
    pg = DSLProgramGenerator([], [])
    p = [1,0,1,0]
    covered = [False]*4
    groups, new_cov = pg.modulus_groups(p, mod=2, covered=covered, match=1)
    # groups for even indices where p==1: indices 0 and 2 -> remainder 0
    assert 0 in groups and groups[0] == 1
    assert new_cov[0] and new_cov[2]


def test_fit_offsets_polynomial():
    pp = PloynomialProgramGenerator([], [])
    offsets = np.array([0.0, 1.0, 2.0, 3.0])
    poly = pp.fit_offsets(offsets)
    # degree of polynomial = max(4, len(sleep_times)) = max(4,3)=4 -> length 5
    assert isinstance(poly, np.ndarray)
    assert poly.shape[0] == 5


def test_gen_file_and_gen_structured_file(tmp_dest):
    # Test that gen_file and gen_structured_file write a new file in dest
    sample = DummySample('s1', offsets=[0.0], max_time=1.0)
    sample.checked = True
    sonic = DummySample('s2', offsets=[0.0], max_time=1.0)
    sonic.checked = True
    lp = LoopProgramGenerator([sample], [sonic], samples_folder=None)
    lp.contents = ''
    # gen_file
    lp.gen_file(tmp_dest)
    files = os.listdir(tmp_dest)
    assert any(name.endswith('.rb') for name in files)
    # clear and test structured
    os.remove(os.path.join(tmp_dest, files[0]))
    lp2 = LoopProgramGenerator([sample], [sonic], samples_folder='/foo')
    lp2.contents = ''
    lp2.gen_structured_file(tmp_dest)
    files2 = os.listdir(tmp_dest)
    assert any(name.endswith('.rb') for name in files2)

if __name__ == "__main__":
    import sys
    errno = pytest.main([__file__])
    sys.exit(errno)