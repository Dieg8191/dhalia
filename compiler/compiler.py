import subprocess

from AST.AST import Program
import os

from AST.function import Function


class Compiler:
    def __init__(self, program: Program):
        self.program = program
        self.c_code = "#include <stdio.h>\n\n" # Basic C code header

        self.vars = {}
        self.functions = {}

    def compile(self) -> str:
        if not isinstance(self.program, Program):
            raise TypeError("Program must be of type Program")

        # The main Function where the program starts
        for func in self.program.functions:
            if func.name == "main":
                origin: Function = func
                break
        else:
            raise ValueError("No main function found in the program")

        self.c_code += origin.c_compile()

        return self.c_code

    def create_c_file(self, filename: str):
        with open(filename, 'w') as f:
            f.write(self.c_code)
        print(f"C code written to {filename}")

    @staticmethod
    def run_compiled(output_file: str):
        dec = "=" * 20

        print(dec + " Running " + dec + ("\n" * 3))
        path = "build/Debug/" + output_file
        subprocess.run([path])


    @staticmethod
    def compile_c(output_file: str, c_file: str):
        build_dir = "build"
        os.makedirs(build_dir, exist_ok=True)

        # Crear CMakeLists.txt
        cmake_file = os.path.join(build_dir, "CMakeLists.txt")
        with open(cmake_file, "w") as f:
            f.write(f"""
                cmake_minimum_required(VERSION 3.20)
                project(MyProgram C)
                set(CMAKE_C_STANDARD 11)
                add_executable({output_file} ../{c_file})
            """)

        # Generar proyecto
        subprocess.run(["cmake", "."], cwd=build_dir, check=True)
        # Compilar
        subprocess.run(["cmake", "--build", "."], cwd=build_dir, check=True)
        print(f"Compiled {c_file} to {output_file} using CMake")


