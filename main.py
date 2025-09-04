import sys
from compiler.DhaliaASTParser.codeProcessor import CodeProcessor
from compiler.compiler import Compiler


def main() -> None:
    compiler = CodeProcessor(sys.argv[1])
    program = compiler.compile()

    c_compiler = Compiler(program)
    c_compiler.compile()
    c_compiler.create_c_file("output.c")
    c_compiler.compile_c("out", "output.c")
    c_compiler.run_compiled("out.exe")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    else:
        print("Usage: python main.py <source_file>")
        sys.exit(1)
