import sexpdata
import synthesis.sonic_pi_dsl as dsl

"""
parses a Rosette generated define form and translates it into our
internal Sonic Pi DSL AST. Uses sexpdata to read S-expressions and
maps each Rosette construct into the corresponding DSL node

main func:
    translate_rosette(rosette_output) -> DSL node

other funcs:
    translate: recursively handle each S-expr form
    translate_define: handle top level (define (f x) ...)
    translate_if: map S-expr if to dsl.If node
"""

def translate_define(ast):
    """
    translate a Rosette define, just want the function body
        (define (beatmapper-fun x) (assume ...) (assume ...) body_expr)
    ignore the assume clauses, if it is just a expression not if statement
    then wrap in dsl.Return
    """
    #["define", [function_name, arg], assumption, assumption, body]
    defn = ast[1]
    func_name = str(defn[0])
    arg = str(defn[1])
    body = translate(ast[4])
    #print("body", body)
    if not isinstance(body, dsl.If):
        if isinstance(body, dsl.Int):
            if body.x == 1:
                body = dsl.Bool("true")
            elif body.x == 0:
                body = dsl.Bool("false")
        body = dsl.Return(body)
    return body

def translate_if(ast):
    """
    translate a Rosette if - 
        (if cond then else)
    wrapping the branches in return statement
    """
    # ["if", condition, then, else]
    if ast[1] == sexpdata.Symbol("#f"):
        return translate(ast[3])
    elif ast[1] == sexpdata.Symbol("#t"):
        return translate(ast[2])
    condition = translate(ast[1])
    then = translate(ast[2])
    #print("then", then)
    if not isinstance(then, dsl.If):
        if isinstance(then, dsl.Int):
            if then.x == 1:
                then = dsl.Bool("true")
            elif then.x == 0:
                then = dsl.Bool("false")
        then = dsl.Return(then)
    else_branch = translate(ast[3])
    #print("else", else_branch)
    if not isinstance(else_branch, dsl.If):
        if isinstance(else_branch, dsl.Int):
            if else_branch.x == 1:
                else_branch = dsl.Bool("true")
            elif else_branch.x == 0:
                else_branch = dsl.Bool("false")
        else_branch = dsl.Return(else_branch)
    return dsl.If([condition], [then, else_branch])


def translate(ast):
    """
    recursively translate any sexpdata node into DSL AST
        - defines and ifs
        - arithmetic and bitvector ops (bveq, bvadd, ...)
        - boolean logic (and, or, not, even?, ...)
        - literals (#t, #f, (bv ...), (int32 ...))
        - default function calls
    """
    #print(ast)
    if isinstance(ast, list):
        head = ast[0]
        if head == sexpdata.Symbol("define"):
            return translate_define(ast)
        elif head == sexpdata.Symbol("if"):
            return translate_if(ast)
        elif head == sexpdata.Symbol("x"):
            return dsl.Int("x")
        elif head == sexpdata.Symbol("int32"):
            #e.g. 2 is in form (int32 2)
            return translate(ast[1])
        elif head == sexpdata.Symbol("bv"):
            #e.g. 2 is in form (bv #x00000002 32)
            return dsl.Int(int(ast[1][2:], base=16))
        elif head == sexpdata.Symbol("=") or head == sexpdata.Symbol("bveq"):
            left = translate(ast[1])
            right = translate(ast[2])
            return dsl.Eq(left, right)
        elif head == sexpdata.Symbol("<") or head == sexpdata.Symbol("bvslt"):
            left = translate(ast[1])
            right = translate(ast[2])
            return dsl.LT(left, right)
        elif head == sexpdata.Symbol("<=") or head == sexpdata.Symbol("bvsle"):
            left = translate(ast[1])
            right = translate(ast[2])
            return dsl.LE(left, right)
        elif head == sexpdata.Symbol(">") or head == sexpdata.Symbol("bvsgt"):
            left = translate(ast[1])
            right = translate(ast[2])
            return dsl.GT(left, right)
        elif head == sexpdata.Symbol(">=") or head == sexpdata.Symbol("bvsge"):
            left = translate(ast[1])
            right = translate(ast[2])
            return dsl.GE(left, right)
        elif head == sexpdata.Symbol("&&"):
            left = translate(ast[1])
            right = translate(ast[2])
            return dsl.And(left, right)
        elif head == sexpdata.Symbol("||"):
            left = translate(ast[1])
            right = translate(ast[2])
            return dsl.Or(left, right)
        elif head == sexpdata.Symbol("even?") or head == sexpdata.Symbol("bveven?"):
            arg = translate(ast[1])
            return dsl.Eq(dsl.Mod(arg, dsl.Int(2)), dsl.Int(0))
        elif head == sexpdata.Symbol("odd?") or head == sexpdata.Symbol("bvodd?"):
            arg = translate(ast[1])
            return dsl.Eq(dsl.Mod(arg, dsl.Int(2)), dsl.Int(1))
        elif head == sexpdata.Symbol("zero?") or head == sexpdata.Symbol("bvzero?"):
            arg = translate(ast[1])
            return dsl.Eq(arg, dsl.Int(0))
        elif head == sexpdata.Symbol("positive?"):
            arg = translate(ast[1])
            return dsl.GT(arg, dsl.Int(0))
        elif head == sexpdata.Symbol("negative?"):
            arg = translate(ast[1])
            return dsl.LT(arg, 0)
        elif head == sexpdata.Symbol("and"):
            #left = translate(ast[1])
            #right = translate(ast[2])
            #return dsl.And(left, right)
            conds = []
            for i in range(1, len(ast)):
                conds.append(translate(ast[i]))
            if len(conds) == 1:
                return conds[0]
            else:
                return dsl.And(conds)
        elif head == sexpdata.Symbol("or"):
            conds = []
            for i in range(1, len(ast)):
                conds.append(translate(ast[i]))
            if len(conds) == 1:
                return conds[0]
            else:
                return dsl.Or(conds)
        elif head == sexpdata.Symbol("not"):
            arg = translate(ast[1])
            return dsl.Not(arg)
        elif head == sexpdata.Symbol("modulo") or head == sexpdata.Symbol("bvsmod"):
            left = translate(ast[1])
            right = translate(ast[2])
            return dsl.Mod(left, right)
        elif head == sexpdata.Symbol("quotient") or head == sexpdata.Symbol("bvsdiv"):
            left = translate(ast[1])
            right = translate(ast[2])
            return dsl.Div(dsl.Sub(left, dsl.Mod(left, right)), right)
        elif head == sexpdata.Symbol("+") or head == sexpdata.Symbol("bvadd"):
            left = translate(ast[1])
            right = translate(ast[2])
            return dsl.Plus(left, right)
        elif head == sexpdata.Symbol("-") or head == sexpdata.Symbol("bvsub"):
            left = translate(ast[1])
            right = translate(ast[2])
            return dsl.Sub(left, right)
        elif head == sexpdata.Symbol("*") or head == sexpdata.Symbol("bvmul"):
            left = translate(ast[1])
            right = translate(ast[2])
            return dsl.Mult(left, right)
        elif head == sexpdata.Symbol("add1") or head == sexpdata.Symbol("bvadd1"):
            arg = translate(ast[1])
            return dsl.Plus(arg, dsl.Int(1))
        elif head == sexpdata.Symbol("sub1") or head == sexpdata.Symbol("bvsub1"):
            arg = translate(ast[1])
            return dsl.Sub(arg, dsl.Int(1))
        elif head == sexpdata.Symbol("bvnot"):
            #bitwise negation gives twos compliment -1 (negation minus 1)
            arg = translate(ast[1])
            return dsl.Sub(dsl.Mult(arg, dsl.Int(-1)), dsl.Int(1))
        elif head == sexpdata.Symbol("bvneg"):
            arg = translate(ast[1])
            return dsl.Mult(arg, dsl.Int(-1))
        elif head == sexpdata.Symbol("bvand"):
            pass
        elif head == sexpdata.Symbol("bvor"):
            pass
        elif head == sexpdata.Symbol("bvshl"):
            # left shift (doubles number for every shift)
            arg = translate(ast[1])
            power = translate(ast[2])
            return dsl.Mult(arg, dsl.Power(dsl.Int(2), power))
        elif head == sexpdata.Symbol("bvashr"):
            # arithmetic right shift (halfs number for every shift)
            arg = translate(ast[1])
            power = translate(ast[2])
            return dsl.Mult(arg, dsl.Power(dsl.Float(0.5), power))
        elif head == sexpdata.Symbol("bvxor"):
            pass
        elif head == sexpdata.Symbol("assume"):
            return dsl.Expr("")
        elif head == sexpdata.Symbol("assert"):
            return translate(ast[1])
        elif head == sexpdata.Symbol("??"):
            # (?? int32?) sometimes given when they want non zero integer
            return dsl.Int(1)
        elif head == sexpdata.Symbol("bvdiv4?"):
            arg = translate(ast[1])
            return dsl.Eq(dsl.Mod(arg, dsl.Int(4)), dsl.Int(0))
        elif head == sexpdata.Symbol("bvdiv8?"):
            arg = translate(ast[1])
            return dsl.Eq(dsl.Mod(arg, dsl.Int(8)), dsl.Int(0))
        elif head == sexpdata.Symbol("bvdiv3?"):
            arg = translate(ast[1])
            return dsl.Eq(dsl.Mod(arg, dsl.Int(3)), dsl.Int(0))
        elif head == sexpdata.Symbol("bvdiv5?"):
            arg = translate(ast[1])
            return dsl.Eq(dsl.Mod(arg, dsl.Int(5)), dsl.Int(0))
        elif head == sexpdata.Symbol("bvdiv6?"):
            arg = translate(ast[1])
            return dsl.Eq(dsl.Mod(arg, dsl.Int(6)), dsl.Int(0))
        elif head == sexpdata.Symbol("bvdiv7?"):
            arg = translate(ast[1])
            return dsl.Eq(dsl.Mod(arg, dsl.Int(7)), dsl.Int(0))
        elif head == sexpdata.Symbol("bvdiv9?"):
            arg = translate(ast[1])
            return dsl.Eq(dsl.Mod(arg, dsl.Int(9)), dsl.Int(0))
        elif head == sexpdata.Symbol("bvdiv?"):
            arg1 = translate(ast[1]) # modular value
            arg2 = translate(ast[2]) # x + c
            return dsl.Eq(dsl.Mod(arg2, arg1), dsl.Int(0))
        elif head == sexpdata.Symbol("false?"):
            arg = translate(ast[1])
            return dsl.Eq(arg, dsl.Bool("false"))
        else:
            func = str(head)
            args = [translate(a) for a in ast[1:]]
            if args:
                return dsl.FunctionCall(func, args[0])
            else:
                return dsl.FunctionCall(func, args[0])
    else:
        # ast is number, bool or variable
        if ast == sexpdata.Symbol("#t"):
            return dsl.Bool("true")
        elif ast == sexpdata.Symbol("#f"):
            return dsl.Bool("false")
        elif isinstance(ast, sexpdata.Symbol):
            return dsl.Expr(str(ast))
        elif isinstance(ast, bool):
            return dsl.Bool("true") if ast else dsl.Bool("false")
        else:
            return dsl.Int(ast) if isinstance(ast, int) else dsl.Expr(str(ast))

def translate_rosette(rosette_func):
    """
    given the output of Rosette extract Sonic Pi DSL
    """
    #print(rosette_func)
    start = rosette_func.find("(define")
    rosette_func = rosette_func[start:]
    print(rosette_func)
    parsed = sexpdata.loads(rosette_func)
    #print(parsed)
    dsl_func = translate(parsed)
    return dsl_func

#print(translate_rosette("(define (beatmapper-fun x) (even? x))").to_code())
#print(translate_rosette("(define (beatmapper-fun x) (if (= (add1 0) x) #f (if (= 7 x) (if #f #t #f) x)))").to_code())
#print(int("0000002d", base=16))

func = """(define (betmapper-sketch x)
(assume (bvsge x (int32 0)))
(assume (bvsle x (int32 30)))
  (if (bvdiv4? x)
      #t
      (if (bvzero? x) #t #f)
      )
  )"""
#parsed = sexpdata.loads(func)
#dsl_fun = translate(parsed)
#print(dsl_fun.to_code())