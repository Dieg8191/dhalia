from AST.AST import Function


class FnCompiler:
    @staticmethod
    def compile_function(function: Function) -> str:
        c = f"int {function.name}() {{"


        return c + "\n}"

