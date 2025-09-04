from compiler.AST.AST import *
from compiler.AST.dataTypes import String, Number
from compiler.AST.function import FnArgument, Function, FnCall
from compiler.AST.logStatement import LogStatement
from compiler.AST.operators import *
from compiler.AST.variables import VarDeclaration, Variable


class Parser:
    def __init__(self, tokens: list[str]):
        self.tokens = tokens
        self.pos = 0
        self.var_types = {"int", "string", "float", "bool"}
        self.reserved_keywords = {"fn", "log"} | self.var_types

    def parse(self) -> Program:
        functions = []
        while self.current_token() is not None:
            functions.append(self.parse_fn())

        return Program(functions)

    def current_token(self) -> str:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def get_next_token(self) -> str | None:
        return self.tokens[self.pos + 1] if self.pos < len(self.tokens) - 1 else None

    def require(self, expected_token: str) -> None:
        if expected_token != self.current_token():
            raise SyntaxError(f"Expected token '{expected_token}', but found '{self.current_token()}'")
        self.advance()

    def advance(self) -> None:
        self.pos += 1

    def valid_name(self, name: str) -> bool:
        return name.isidentifier() and not name in self.reserved_keywords

    def parse_fn_args(self) -> FnArgument:
        if not self.current_token() in self.var_types:
            raise SyntaxError(f"Invalid variable type '{self.current_token()}'")

        var_type = self.current_token()
        self.advance()

        name = self.current_token()
        if not self.valid_name(name):
            raise SyntaxError(f"Invalid variable name '{name}'")
        self.advance()

        return FnArgument(var_type, name)

    def parse_fn(self):
        self.require("fn")
        name = self.current_token()
        if not self.valid_name(name):
            raise SyntaxError(f"Invalid function name '{name}'")
        self.advance()

        args = []
        if self.current_token() == "(":
            self.require("(")
            while self.current_token() != ")":
                args.append(self.parse_fn_args())
            self.require(")")

        self.require("{")

        body = []
        while self.current_token() != "}":
            body.append(self.parse_statement())
        self.require("}")
        return Function(name, args, body)

    def parse_var(self):
        var_type = self.current_token()
        self.advance()

        mutable = True
        if self.current_token() in ("mutable", "immutable"):
            mutable = self.current_token() != "inmutable"
            self.advance()

        name = self.current_token()
        if not self.valid_name(name):
            raise SyntaxError(f"Invalid variable name '{name}'")
        self.advance()

        self.require("=")
        expr = self.parse_expression()
        self.require(";")

        return VarDeclaration(var_type, name, mutable, expr)

    def parse_statement(self):
        token = self.current_token()

        if token == "log":
            return self.parse_log()
        elif self.current_token() in self.var_types:
            return self.parse_var()

        expr = self.parse_expression()
        self.require(";")

        return expr

    def parse_string(self):
        if not self.is_string(self.current_token()):
            raise SyntaxError(f"Invalid string literal: '{self.current_token()}'")

        value = self.current_token().replace('"', '')
        self.advance()

        return String(value)

    @staticmethod
    def is_string(token: str) -> bool | str:
        return token.startswith('"') and token.endswith('"')

    def parse_expression(self):
        if self.is_string(self.current_token()):
            return self.parse_string()

        elif self.current_token().isnumeric():  # Integer literal
            value = int(self.current_token())
            self.advance()
            return Number(value)

        elif self.current_token() == "+":
            self.advance()
            return Addition()

        elif self.current_token() == "-":
            self.advance()
            return Subtraction()

        elif self.current_token() == "*":
            self.advance()
            return Multiplication()

        elif self.current_token() == "/":
            self.advance()
            return Division()

        elif self.get_next_token() != "(":  # Not a Function call
            var_name = self.current_token()
            self.advance()
            return Variable(var_name)

        elif self.valid_name(self.current_token()):
            name = self.current_token()
            self.advance()
            self.require("(")

            args = []
            while self.current_token() != ")":
                args.append(self.parse_expression())
                if self.current_token() == ",":
                    self.require(",")

            self.require(")")
            return FnCall(name, args)

        raise SyntaxError(f"Invalid expression '{self.current_token()}'")

    def parse_log(self):
        self.require("log")
        self.require("(")

        expr = []
        while self.current_token() != ")":
            expr.append(self.parse_expression())

        self.require(")")
        self.require(";")
        return LogStatement(expr)
