from .AST import Expression


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