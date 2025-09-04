from .AST import Expression


class LogStatement(Expression):
    def __init__(self, arg: list[Expression]):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return f"LogStatement: {self.arg}"

    def c_compile(self) -> str:
        compiled_args = [a.c_compile() for a in self.arg]
        return f"printf({"".join(compiled_args)})"