from .AST import Expression
from typing import Optional
from ..exceptions.compileErrors import CompileError


class LogStatement(Expression):
    def __init__(self, arg: list[Expression], sep: Optional[str] = ", "):
        super().__init__()
        self.args = arg
        self.sep = sep

    def __repr__(self):
        return f"LogStatement: {self.args}"

    def c_compile(self) -> str:
        return f"printf({self.compile_args()})"

    def compile_args(self) -> str:
        compiled_args = [a.c_compile() for a in self.args]

        if not isinstance(compiled_args[0], str):
            raise CompileError("First argument of a Log Statement should be type String.")

        origin = compiled_args[0][:-2] # Deletes  ->  \"

        values = []
        if len(compiled_args) > 1:
            for expr in compiled_args[1:]:
                origin += " "
                if expr.isnumeric():
                    origin += "%d"
                else:
                    origin += "%s"
                values.append(expr)

        origin += "\""
        if values:
            return rf'{origin}, {", ".join(map(str, values))}'
        else:
            return rf'{origin}'