import pytest
import synthesis.sonic_pi_dsl as dsl


def test_program_to_code():
    prog = dsl.Program([dsl.Expr('a'), dsl.Expr('b')])
    code = prog.to_code()
    assert code == 'a\nb'


def test_live_loop_to_code():
    # Body contains a single sleep
    body = [dsl.Sleep(dsl.Expr('0.5'))]
    loop = dsl.LiveLoop('beat', body)
    out = loop.to_code()
    expected = 'live_loop :beat do\n\tsleep 0.5\nend'
    assert out == expected


def test_sample_variants():
    # No params, no condition
    s1 = dsl.Sample(':kick')
    assert s1.to_code() == 'sample :kick'
    # With parameters only
    params = dsl.Env((0.1,0.2,0.3,0.4,0.5,1,0.8,0.6))
    s2 = dsl.Sample(':snare', parameters=params)
    assert s2.to_code() == 'sample :snare, ' + params.to_code()
    # With condition only
    cond = dsl.Eq(dsl.Expr('x'), dsl.Expr('y'))
    s3 = dsl.Sample(':hihat', condition=cond)
    assert s3.to_code() == 'sample :hihat if x == y'
    # With both
    s4 = dsl.Sample(':hat', parameters=params, condition=cond)
    assert s4.to_code() == 'sample :hat, ' + params.to_code() + ' if x == y'


def test_env_to_code():
    values = (1,2,3,4,5,0.1,0.2,0.3)
    env = dsl.Env(values)
    code = env.to_code()
    assert 'start: 1' in code
    assert 'attack: 2' in code
    assert 'release: 5' in code


def test_sleep_and_expr():
    e = dsl.Expr('42')
    sleep = dsl.Sleep(e)
    assert sleep.to_code() == 'sleep 42'
    # Expr should include indent
    assert dsl.Expr('foo').to_code('  ') == '  foo'


def test_function_to_code():
    body = [dsl.Expr('1')]
    fn1 = dsl.Function('foo', body)
    out1 = fn1.to_code()
    assert out1.startswith('define :foo do ')
    fn2 = dsl.Function('bar', body, argument='arg')
    out2 = fn2.to_code()
    assert 'define :bar do |arg|' in out2


def test_var_mod():
    v = dsl.Var('x', dsl.Expr('val'))
    assert v.to_code() == 'set :x, val'
    m = dsl.Mod(dsl.Expr('i'), dsl.Expr('n'))
    assert m.to_code() == 'i % n'


def test_comparisons():
    cmp = [dsl.LT, dsl.LE, dsl.GT, dsl.GE, dsl.Eq]
    ops = ['<','<=','>','>=','==']
    for cls, op in zip(cmp, ops):
        node = cls(dsl.Expr('a'), dsl.Expr('b'))
        assert op in node.to_code()


def test_logical_and_or_not():
    conds = [dsl.LT(dsl.Expr('a'), dsl.Expr('b')), dsl.GT(dsl.Expr('c'), dsl.Expr('d'))]
    a = dsl.And(conds)
    o = dsl.Or(conds)
    assert '&&' in a.to_code()
    assert '||' in o.to_code()
    n = dsl.Not(conds[0])
    assert 'not(' in n.to_code()


def test_ring_and_range():
    r = dsl.Ring('r', ['1','2','3'])
    assert r.to_code() == 'r = (ring 1,2,3)'
    rg = dsl.Range('x', dsl.Int(0), dsl.Int(5), dsl.Int(1))
    assert 'range(0, 5, 1)' in rg.to_code()


def test_if_to_code():
    cond = dsl.Eq(dsl.Expr('x'), dsl.Expr('y'))
    body = dsl.Expr('z')
    if_node = dsl.If([cond], [body])
    code = if_node.to_code()
    lines = code.splitlines()
    assert lines[0] == 'if x == y'
    assert lines[1].strip() == 'z'
    assert lines[-1] == 'end'


def test_return_math_ops_tick():
    ret = dsl.Return(dsl.Expr('v'))
    assert ret.to_code() == 'return v'
    # Math
    plus = dsl.Plus(dsl.Expr('1'), dsl.Expr('2'))
    assert '(1 + 2)' in plus.to_code()
    assert '(3 - 4)' in dsl.Sub(dsl.Expr('3'), dsl.Expr('4')).to_code()
    assert '(5 * 6)' in dsl.Mult(dsl.Expr('5'), dsl.Expr('6')).to_code()
    assert '(7 / 8)' in dsl.Div(dsl.Expr('7'), dsl.Expr('8')).to_code()
    assert '(9 ** 10)' in dsl.Power(dsl.Expr('9'), dsl.Expr('10')).to_code()
    # Tick
    t = dsl.Tick('i', 'r')
    assert t.to_code() == 'i = r.tick().to_i'


def test_literals_and_get():
    assert dsl.Int(3).to_code() == '3'
    assert dsl.Bool('true').to_code() == 'true'
    nv = dsl.NumVar('x', dsl.Int(5))
    assert nv.to_code() == 'x = 5'
    assert dsl.Float(1.23).to_code() == '1.23'
    assert dsl.Get('foo').to_code() == 'get[:foo]'


def test_samplefolder_and_cue_sync_print_call_tempo():
    sf = dsl.SampleFolder('samples', '/path')
    assert "samples = '/path'" == sf.to_code()
    cue = dsl.Cue('go')
    assert "cue 'go'" == cue.to_code()
    sync = dsl.Sync('back')
    assert "sync 'back'" == sync.to_code()
    pr = dsl.Print('msg')
    assert "print msg" == pr.to_code()
    fc1 = dsl.FunctionCall('foo', dsl.Expr('x'))
    assert fc1.to_code() == 'foo(x)'
    fc2 = dsl.FunctionCall('bar')
    assert fc2.to_code() == 'bar()'
    tempo = dsl.Tempo(120)
    assert tempo.to_code() == 'use_bpm 120'


if __name__ == "__main__":
    import sys
    errno = pytest.main([__file__])
    sys.exit(errno)
    