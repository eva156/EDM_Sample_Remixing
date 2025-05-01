import pytest
import sexpdata
import synthesis.rosette_translator as rt
import synthesis.sonic_pi_dsl as dsl


# Helpers
S = sexpdata.Symbol

# Test translate_define with non-if body wraps in Return
def test_translate_define_simple():
    # AST: (define (f x) (assume ...) (assume ...) x)
    ast = [S('define'), [S('f'), S('x')], ['assume', S('a')], ['assume', S('b')], S('x')]
    result = rt.translate_define(ast)
    # Should be a Return node wrapping Expr('x')
    assert isinstance(result, dsl.Return)
    assert result.to_code() == 'return x'

# Test translate_define with if body returns If node
def test_translate_define_if_body():
    # AST: define with if as body
    cond = [S('='), S('x'), 1]
    then = 2
    els = 3
    ast = [S('define'), [S('f'), S('x')], ['assume', S('a')], ['assume', S('b')], [S('if'), cond, then, els]]
    result = rt.translate_define(ast)
    # Should be an If DSL node, not wrapped in Return
    assert isinstance(result, dsl.If)
    # to_code should include 'if x == 1'
    code = result.to_code()
    assert code.startswith('if x == 1')
    assert 'return 2' in code and 'return 3' in code

# Test translate_if handles always-false condition (#f)
def test_translate_if_false_condition():
    body_true = ['dummy']
    body_else = S('y')
    ast = [S('if'), S('#f'), body_true, body_else]
    # translate_if should return translate of else branch: Expr('y')
    result = rt.translate_if(ast)
    assert isinstance(result, dsl.Expr)
    assert result.to_code() == 'y'

# Test translate_if handles always-true condition (#t)
def test_translate_if_true_condition():
    then = S('z')
    els = S('w')
    ast = [S('if'), S('#t'), then, els]
    result = rt.translate_if(ast)
    assert isinstance(result, dsl.Expr)
    assert result.to_code() == 'z'

# Test translate basic types
@pytest.mark.parametrize('val,expected', [
    (S('#t'), 'true'),
    (S('#f'), 'false'),
    (True, 'true'),
    (False, 'false'),
    (42, '42'),
])
def test_translate_literals(val, expected):
    node = rt.translate(val)
    assert hasattr(node, 'to_code')
    assert node.to_code() == expected

# Test translate symbol
def test_translate_symbol():
    node = rt.translate(S('foo'))
    assert isinstance(node, dsl.Expr)
    assert node.to_code() == 'foo'

# Test translate int32
def test_translate_int32():
    ast = [S('int32'), 7]
    node = rt.translate(ast)
    assert isinstance(node, dsl.Int)
    assert node.to_code() == '7'

# Test translate bv hex
def test_translate_bv_hex():
    ast = [S('bv'), '#x0000000A', 32]
    node = rt.translate(ast)
    assert isinstance(node, dsl.Int)
    assert node.to_code() == '10'

# Test arithmetic and equality operators
@pytest.mark.parametrize('op,cls,codeop', [
    ('=', dsl.Eq, '=='),
    ('<', dsl.LT, '<'),
    ('<=', dsl.LE, '<='),
    ('>', dsl.GT, '>'),
    ('>=', dsl.GE, '>='),
])
def test_translate_comparisons(op, cls, codeop):
    ast = [S(op), 1, 2]
    node = rt.translate(ast)
    assert isinstance(node, cls)
    c = node.to_code()
    assert codeop in c

# Test plus, minus, mult, div
@pytest.mark.parametrize('op,cls,codeop', [
    ('+', dsl.Plus, '+'),
    ('-', dsl.Sub, '-'),
    ('*', dsl.Mult, '*'),
    ('modulo', dsl.Mod, '%'),
])
def test_translate_arithmetic(op, cls, codeop):
    ast = [S(op), 3, 4]
    node = rt.translate(ast)
    assert isinstance(node, cls)
    assert codeop in node.to_code()

# Test boolean and/or/not
def test_translate_and_or_not():
    a = [S('and'), [S('='),1,1],[S('<'),1,2]]
    node = rt.translate(a)
    assert isinstance(node, dsl.And)
    o = [S('or'), [S('='),1,1],[S('>'),3,2]]
    node2 = rt.translate(o)
    assert isinstance(node2, dsl.Or)
    n = [S('not'), [S('='),1,1]]
    node3 = rt.translate(n)
    assert isinstance(node3, dsl.Not)

# Test assume and assert
def test_translate_assume_assert():
    ast_assume = [S('assume'), 1]
    node = rt.translate(ast_assume)
    # assume yields empty Expr
    assert isinstance(node, dsl.Expr)
    assert node.to_code() == ''
    ast_assert = [S('assert'), [S('='),1,1]]
    node2 = rt.translate(ast_assert)
    assert isinstance(node2, dsl.Eq)

# Test function call default
def test_translate_function_call():
    ast = [S('foo'), 5]
    node = rt.translate(ast)
    assert isinstance(node, dsl.FunctionCall)
    assert node.to_code().startswith('foo(')

# Test translate_rosette with if inside
def test_translate_rosette_define_if():
    code = "(define (g y) (assume _) (assume _) (if (< y (int32 5)) (int32 1) (int32 0)))"
    node = rt.translate_rosette(code)
    assert isinstance(node, dsl.If)
    out = node.to_code()
    assert 'if y < 5' in out or 'if' in out

if __name__ == "__main__":
    import sys
    errno = pytest.main([__file__])
    sys.exit(errno)