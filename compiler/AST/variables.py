from .AST import Expression


class VarDeclaration(Expression):
    def __init__(self, var_type, name, mutable, value):
        self.name = name
        self.type = var_type
        self.mutable = mutable
        self.value = value
        self.c_var_eq = {
            "int": "int",
            "string" : "char*",
            "float": "float",
            "bool": "int"
        }

    def __repr__(self):
        return f"VarDeclaration: name={self.name}, type={self.type}, mutable={self.mutable}, value={self.value}"

    def c_compile(self) -> str:
        return f"{self.c_var_eq[self.type]} {self.name} = {self.value.c_compile()}"


class Variable(Expression):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f"Variable: {self.name}"

    def c_compile(self) -> str:
        return f"{self.name}"