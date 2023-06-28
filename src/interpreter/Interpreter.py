import sys
from typing import Any

from src.interpreter.RunningRuntimeError import RunningRuntimeError

from antlr4.InputStream import InputStream
from src.grammar.SmallerBasicLexer import SmallerBasicLexer
from src.grammar.SmallerBasicParser import SmallerBasicParser

class Interpreter(object):
    def __init__(self):
        self.__source_code: Any = None
        self.__is_running: bool = False 

    def load_file(self, file_path: str) -> None:
        """
        Load the source code from a file and split it into lines.

        Args:
            file_path (str): The path to the source code file.
        """
        if self.__is_running:
            raise RunningRuntimeError(self.load_file.__name__, self.__is_running)

        with open(file_path, encoding="UTF-8", mode="r") as file:
            self.source_code = file.read()

        if self.__source_code is not None:
            self.split_source_code(self.source_code)

    def split_source_code(self, source_code: str) -> None:
        """
        Split the source code into lines.

        Args:
            source_code (str): The source code.
        """
        if self.__is_running:
            raise RunningRuntimeError(self.load_file.__name__, self.__is_running)

        self.__source_code = source_code.splitlines()
    
    def run(self, file_path):
        """
        Run the interpreter.

        Args:
            file_path (str): The path to the source code file.
        """
        self.load_file(file_path)

        if self.__source_code is not None:
            self.__is_running = True
        
        input_stream: InputStream = InputStream(self.__source_code)
        lexer: SmallerBasicLexer = SmallerBasicLexer(input_stream) 

        self.__is_running = False
    
