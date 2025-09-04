from .AST import Expression


class Addition(Expression): # TODO: Implement left and right hands for operations
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"Addition"

    def c_compile(self) -> str:
        raise NotImplementedError


class Division(Expression): # TODO: Implement left and right hands for operations
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"Division"

    def c_compile(self) -> str:
        raise NotImplementedError


class Multiplication(Expression): # TODO: Implement left and right hands for operations
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"Multiplication"

    def c_compile(self) -> str:
        raise NotImplementedError


class Subtraction(Expression): # TODO: Implement left and right hands for operations
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"Subtraction"

    def c_compile(self) -> str:
        raise NotImplementedError