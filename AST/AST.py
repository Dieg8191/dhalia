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
