import re
from compiler.DhaliaASTParser.colors import Colors
from compiler.AST.AST import Program
from compiler.DhaliaASTParser.parser import Parser
import sys

class CodeProcessor:
    def __init__(self, path: str):
        try:
            with open(path, 'r') as f:
                self.source_code = f.read()

        except FileNotFoundError:
            print(f"Error: The file {path} was not found.")
            sys.exit(1)

    def tokenize(self):
        tokens = re.findall(r"\".*?\"|\w+|[{}();=+\-/*]", self.source_code)

        return tokens

    def compile(self)  -> Program:
        parser = Parser(self.tokenize())
        program: Program = parser.parse()

        main_fn = None

        for fn in program.functions:
            if fn.name == "main":
                main_fn = fn
                break

        if main_fn is None:
            print(f"{Colors.RED}Error: {Colors.RESET}The {Colors.YELLOW}main {Colors.RESET}function was not found.")
            sys.exit(1)

        return program