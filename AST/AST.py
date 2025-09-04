from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def c_compile(self) -> str:
        pass

class Program:
    def __init__(self, functions):
        self.functions = functions

    def __repr__(self):
        return f"Program: {self.functions}"

class FnArgument(Expression):
    def __init__(self, arg_type, name):
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


class LogStatement(Expression):
    def __init__(self, arg: list[Expression]):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return f"LogStatement: {self.arg}"

    def c_compile(self) -> str:
        compiled_args = [a.c_compile() for a in self.arg]
        return f"printf({"".join(compiled_args)})"


class String(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"String: {self.value}"

    def c_compile(self) -> str:
        return f"\"{self.value}\""


class FnCall(Expression):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __repr__(self):
        return f"FnCall: {self.name}, Args: {self.args}"

    def c_compile(self) -> str:
        pass # TODO: Implement



class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Variable: {self.name}"

    def c_compile(self) -> str:
        pass # TODO: Implement


class Addition(Expression): # TODO: Implement left and right hands for operations
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"Addition"

    def c_compile(self) -> str:
        pass # TODO: Implement


class Division(Expression): # TODO: Implement left and right hands for operations
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"Division"

    def c_compile(self) -> str:
        pass # TODO: Implement


class Multiplication(Expression): # TODO: Implement left and right hands for operations
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"Multiplication"

    def c_compile(self) -> str:
        pass # TODO: Implement


class Subtraction(Expression): # TODO: Implement left and right hands for operations
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"Subtraction"

    def c_compile(self) -> str:
        pass # TODO: Implement


class Number(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number: {self.value}"

    def c_compile(self) -> str:
        return str(self.value)

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