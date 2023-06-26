from src.grammar import SmallerBasicLexer
from src.grammar import SmallerBasicParser

import sys
from typing import Any

class Interpreter(object):
    def __init__(self):
        self.__source_code: Any = None
    
    def load_file(self, file_path: str):
        with open(file_path, encoding="UTF-8", mode="r") as file:
            self.__source_code = file.read().splitlines()
        print(self.__source_code)

