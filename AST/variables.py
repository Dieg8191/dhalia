from .AST import Expression


class VarDeclaration(Expression):
    def __init__(self, var_type, name, mutable, value):
        self.name = name
        self.type = var_type
        self.mutable = mutable
        self.value = value

    def __repr__(self):
        return f"VarDeclaration: name={self.name}, type={self.type}, mutable={self.mutable}, value={self.value}"

    def c_compile(self) -> str:
        pass # TODO: Implement


class Variable(Expression):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f"Variable: {self.name}"

    def c_compile(self) -> str:
        pass # TODO: Implement