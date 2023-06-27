import sys
from typing import Any

from antlr4.InputStream import InputStream

from src.grammar import SmallerBasicLexer
from src.grammar import SmallerBasicParser

class Interpreter(object):
    def __init__(self):
        self.__source_code: Any          = None
        self.__is_running: bool          = False

    def load_file(self, file_path: str) -> None:
        """
        Load the source code from a file and split it into lines.

        Args:
            file_path (str): The path to the source code file.
        """
        with open(file_path, encoding="UTF-8", mode="r") as file:
            self.__source_code = file.read()

        if self.__source_code is not None:
            self.split_source_code(self.__source_code)

    def split_source_code(self, source_code: str) -> None:
        """
        Split the source code into lines.
        """
        self.source_code = source_code.splitlines()
   

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
        lexer: SmallerBasicLexer = SmallerBasicLexer(input_stream)) 
        
     
