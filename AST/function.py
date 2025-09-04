from .AST import Expression


class FnArgument(Expression):
    def __init__(self, arg_type, name):
        super().__init__()
        self.name = name
        self.type = arg_type

    def __repr__(self):
        return f"FnArgument:  type={self.type}, name={self.name}"

    def c_compile(self) -> str:
        return f"{self.type} {self.name}"


class Function(Expression):
    def __init__(self, name, args: list[FnArgument], body: list[Expression]):
        super().__init__()
        self.name = name
        self.args = args
        self.body = body
        self.return_type = "int"  # The default return type is int for simplicity TODO: Make dynamic

    def __repr__(self):
        return f"Function: {self.name}, Args: {self.args}, Body: {self.body}"

    def c_compile(self) -> str:
        compiled_args = []
        for arg in self.args:
            compiled_args.append(arg.c_compile())

        c = f"{self.return_type} {self.name} ({", ".join(compiled_args)}) {{\n"

        for expr in self.body:
            c += f"{expr.c_compile()};\n"

        return c + "\n}"


class FnCall(Expression):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __repr__(self):
        return f"FnCall: {self.name}, Args: {self.args}"

    def c_compile(self) -> str:
        pass # TODO: Implement
