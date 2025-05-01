"""
DSL AST nodes for generating Sonic Pi code
each class represents a language construct and 
implements .to_code() to produce indented syntax
"""

class DSL:
    """
    base interface for all DSL nodes
    """
    def to_code(self, indent=""):
        raise NotImplementedError("to_code not implemented")

class Program(DSL):
    """
    Top-level container for list of elements
    """
    def __init__(self, elements):
        self.elements = elements
    
    def to_code(self, indent=""):
        code = "\n".join(node.to_code(indent) for node in self.elements)
        return code

class LiveLoop(DSL):
    """
    live_loop :name do ... end
    """
    def __init__(self, name, body):
        self.name = name
        self.body = body

    def to_code(self, indent=""):
        code = f"\n".join(node.to_code(f"{indent}\t") for node in self.body)
        return f"{indent}live_loop :{self.name} do\n{code}\nend"
    
class Sample(DSL):
    """
    sample :name, [params] [if condition]
    """
    def __init__(self, sample_name, parameters=None, condition=None):
        self.name = sample_name
        self.if_cond = condition
        self.parameters = parameters # e.g. envelope, amplitude
    
    def to_code(self, indent=""):
        if self.parameters:
            if self.if_cond:
                return f"{indent}sample {self.name}, {self.parameters.to_code()} if {self.if_cond.to_code()}"
            else:
                return f"{indent}sample {self.name}, {self.parameters.to_code()}"
        else:
            if self.if_cond:
                return f"{indent}sample {self.name} if {self.if_cond.to_code()}"
            else:
                return f"{indent}sample {self.name}"

class Env(DSL):
    """
    sample: start, attack, decay, sustain, release and levels
    """
    def __init__(self, env):
        self.start = env[0]
        self.attack = env[1]
        self.decay = env[2]
        self.sustain = env[3]
        self.release = env[4]
        self.attack_level = env[5]
        self.decay_level = env[6]
        self.sustain_level = env[7]
    
    def to_code(self, indent=""):
         return f"{indent}start: {self.start}, attack: {self.attack}, attack_level: {self.attack_level}, decay: {self.decay}, decay_level: {self.decay_level}, sustain: {self.sustain}, sustain_level: {self.sustain_level}, release: {self.release}"
        
class Sleep(DSL):
    """
    sleep duration in seconds
    """
    def __init__(self, duration):
        self.duration = duration
    
    def to_code(self, indent=""):
        return f"{indent}sleep {self.duration.to_code()}"

class Expr(DSL):
    """
    expression or literal
    """
    def __init__(self, expr):
        self.expr = expr
    
    def to_code(self, indent=""):
        return indent + self.expr

class Function(DSL):
    """
    define :name |arg| do ... end
    """
    def __init__(self, name, body, argument=None):
        self.name = name
        self.body = body
        self.argument = argument

    def to_code(self, indent=""):
        code = "\n".join(node.to_code(f"{indent}\t") for node in self.body)
        if self.argument:
            return f"{indent}define :{self.name} do |{self.argument}|\n{code}\nend"
        else:
            return f"{indent}define :{self.name} do \n{code}\nend"

class Var(DSL):
    """
    set :name, value
    """
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def to_code(self, indent=""):
        return f"{indent}set :{self.name}, {self.value.to_code()}"


class Mod(DSL):
    """
    x % y
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def to_code(self, indent=""):
        return f"{indent}{self.x.to_code()} % {self.y.to_code()}"

# comparison operators
class LT(DSL):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def to_code(self, indent=""):
        return f"{indent}{self.x.to_code()} < {self.y.to_code()}"

class LE(DSL):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def to_code(self, indent=""):
        return f"{indent}{self.x.to_code()} <= {self.y.to_code()}"

class GT(DSL):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def to_code(self, indent=""):
        return f"{indent}{self.x.to_code()} > {self.y.to_code()}"

class GE(DSL):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def to_code(self, indent=""):
        return f"{indent}{self.x.to_code()} >= {self.y.to_code()}"


class Eq(DSL):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def to_code(self, indent=""):
        return f"{indent}{self.x.to_code()} == {self.y.to_code()}"

# logical operators
class And(DSL):
    def __init__(self, conds):
        self.conds = conds
        #self.cond1 = cond1
        #self.cond2 = cond2
    
    def to_code(self, indent=""):
        conditions = (" && ").join([c.to_code() for c in self.conds])
        return f"{indent}({conditions})"
        #return f"{indent}({self.cond1.to_code()}) && ({self.cond2.to_code()})"

class Or(DSL):
    def __init__(self, conds):
        self.conds = conds
        #self.cond2 = cond2
    
    def to_code(self, indent=""):
        conditions = (" || ").join([c.to_code() for c in self.conds])
        return f"{indent}({conditions})"
        #return f"{indent}({self.cond1.to_code()}) || ({self.cond2.to_code()})"

class Not(DSL):
    def __init__(self, cond):
        self.cond = cond
    
    def to_code(self, indent=""):
        return f"{indent}not({self.cond.to_code()})"

class Ring(DSL):
    """
    var = (ring ...)
    """
    def __init__(self, name, items):
        self.name = name
        self.items = items
    
    def to_code(self, indent=""):
        return indent + self.name + " = (ring " + (",").join(self.items) + ")"
    
class Range(DSL):
    """
    var = range(start, end, step)
    """
    def __init__(self, name, start, end, step):
        self.name = name
        self.start = start
        self.end = end
        self.step = step
    
    def to_code(self, indent=""):
        return indent + self.name + f" = range({self.start.to_code()}, {self.end.to_code()}, {self.step.to_code()})"

class If(DSL):
    """
    if ... elsif ... else ... end
    """
    def __init__(self, conditions, bodies):
        self.conditions = conditions
        self.bodies = bodies
    
    def to_code(self, indent=""):
        print(self.conditions)
        print(self.bodies)
        code = indent + "if " + self.conditions[0].to_code() + "\n" + self.bodies[0].to_code(f"{indent}\t")
        if len(self.conditions) > 1:
            for i,c in enumerate(self.conditions[1:]):
                code += "\n" + indent + "elsif " + c.to_code() + "\n" + self.bodies[1+i].to_code(f"{indent}\t")
        if len(self.bodies) > len(self.conditions):
            code += "\n" + indent + "else " + "\n" + self.bodies[-1].to_code(f"{indent}\t")
        code += "\n" + indent + "end"
        return code

class Return(DSL):
    """
    return x
    """
    def __init__(self, x):
        self.x = x
    
    def to_code(self, indent=""):
        #print(self.x)
        return f"{indent}return {self.x.to_code()}"

# math operations
class Plus(DSL):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_code(self, indent=""):
        return f"{indent}({self.x.to_code()} + {self.y.to_code()})"

class Sub(DSL):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_code(self, indent=""):
        return f"{indent}({self.x.to_code()} - {self.y.to_code()})"

class Mult(DSL):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def to_code(self, indent=""):
        return f"{indent}({self.x.to_code()} * {self.y.to_code()})"

class Div(DSL):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def to_code(self, indent=""):
        return f"{indent}({self.x.to_code()} / {self.y.to_code()})"

class Power(DSL):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def to_code(self, indent=""):
        return f"{indent}({self.x.to_code()} ** {self.y.to_code()})"


class Tick(DSL):
    """
    i = ring.tick()
    """
    def __init__(self, name, ring):
        self.ring = ring
        self.var = name
    
    def to_code(self, indent=""):
        return f"{indent}{self.var} = {self.ring}.tick()"

# boolean and numeric DSL nodes
class Int(DSL):
    def __init__(self, x):
        self.x = x
    
    def to_code(self, indent=""):
        return f"{indent}{self.x}"

class Bool(DSL):
    def __init__(self, x):
        self.x = x
    
    def to_code(self, indent=""):
        return f"{indent}{self.x}"

class NumVar(DSL):
    def __init__(self, name, val):
        self.name = name
        self.val = val
    
    def to_code(self, indent=""):
        return f"{indent}{self.name} = {self.val.to_code()}"

class Float(DSL):
    def __init__(self, x):
        self.x = x
    
    def to_code(self, indent=""):
        return f"{indent}{self.x}"

class Get(DSL):
    """
    get[:var]
    """
    def __init__(self, var):
        self.var = var
    
    def to_code(self, indent=""):
        return f"{indent}get[:{self.var}]"

class SampleFolder(DSL):
    """
    samples = "path"
    """
    def __init__(self, name, path):
        self.name = name
        self.path = path
    
    def to_code(self, indent=""):
        return f"{indent}{self.name} = '{self.path}'"

# synchronisation operators
class Cue(DSL):
    def __init__(self, name):
        self.name = name
    
    def to_code(self, indent=""):
        return f"{indent}cue '{self.name}'"
    
class Sync(DSL):
    def __init__(self, name):
        self.name = name
    
    def to_code(self, indent=""):
        return f"{indent}sync '{self.name}'"

class Print(DSL):
    """
    print ...
    """
    def __init__(self, contents):
        self.contents = contents
    
    def to_code(self, indent=""):
        return f"{indent}print {self.contents}"
    
class FunctionCall(DSL):
    """
    func(arg)
    """
    def __init__(self, func, arg=None):
        self.func = func
        self.arg = arg
    
    def to_code(self, indent=""):
        if self.arg != None:
            return f"{self.func}({self.arg.to_code()})"
        else:
            return f"{self.func}()"
        
class Tempo(DSL):
    """
    use_bpm tempo
    """
    def __init__(self, tempo):
        self.tempo = tempo
    
    def to_code(self, indent=""):
        return f"{indent}use_bpm {self.tempo}"

#program = LiveLoop("pattern", [Sample(":kick"), Sleep(0.5)])
#print(program.to_code())
