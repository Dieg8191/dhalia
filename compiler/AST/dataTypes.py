from .AST import Expression

class String(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"String: {self.value}"

    def c_compile(self) -> str:
        return f"\"{self.value}\""

class Number(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number: {self.value}"

    def c_compile(self) -> str:
        return str(self.value)