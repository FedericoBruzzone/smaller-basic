from typing import Any

from src.utils.color_print import color

from src.interpreter.running_runtime_error import RunningRuntimeError
from src.interpreter.interpreter_helper import build_antlr4_tree_string
from src.interpreter.global_memory import GlobalMemory
from src.interpreter.dispatch_table import DispatchTable
from src.error.smaller_basic_error_listener import SmallerBasicErrorListener
from src.grammar.SmallerBasicLexer import SmallerBasicLexer
from src.grammar.SmallerBasicParser import SmallerBasicParser

from src.abstract_syntax_tree.ast_visitor import SmallerBasicAstVisitor
from src.abstract_syntax_tree.ast import Ast

from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream

class Interpreter(object):
    def __init__(self):
        self.__file_path: str = None
        self.__source_code: Any = None
        self.__is_running: bool = False
        self.__libraries: list = ["IO"]
        self.global_memory: GlobalMemory = GlobalMemory()
        self.dispatch_table: DispatchTable = DispatchTable()

    def load_file(self, file_path: str) -> None:
        """
        Load the source code from a file.

        Args:
            file_path (str): The path to the source code file.
        """
        if self.__is_running:
            raise RunningRuntimeError(self.load_file.__name__, self.__is_running)

        self.__file_path = file_path

        with open(file_path, encoding="UTF-8", mode="r") as file:
            source_code = file.read()

        if source_code is not None:
            self.__source_code = source_code

    def do_lexical_analysis(self) -> CommonTokenStream:
        """
        Do the lexical analysis.

        Returns:
            CommonTokenStream: The token stream.
        """

        if not self.__is_running:
            raise RunningRuntimeError(self.do_lexical_analysis.__name__, self.__is_running)

        self.print("Do the lexical analysis...\n")
        input_stream: InputStream       = InputStream(self.__source_code)
        lexer: SmallerBasicLexer        = SmallerBasicLexer(input_stream)
        token_stream: CommonTokenStream = CommonTokenStream(lexer)
        lexer.reset()
        return token_stream

    def do_parser(self, token_stream: CommonTokenStream, print_res: bool = False) -> SmallerBasicParser.ProgramContext:
        """
        Do the parser.

        Args:
            token_stream (CommonTokenStream): The token stream.
            print_res (bool, optional): Whether to print the result. Defaults to False.

        Returns:
            SmallerBasicParser.ProgramContext: The AST.
        """
        if not self.__is_running:
            raise RunningRuntimeError(self.do_parser.__name__, self.__is_running)

        self.print("Do the parser...\n")
        parser: SmallerBasicParser = SmallerBasicParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(SmallerBasicErrorListener())
        smaller_basic_tree: SmallerBasicParser.ProgramContext = parser.program()
        if print_res:
            self.print(build_antlr4_tree_string(smaller_basic_tree.toStringTree(recog = parser)))
        if parser.getNumberOfSyntaxErrors() > 0:
            print()
            raise SyntaxError("There is syntax error in the source code.")
        return smaller_basic_tree

    def create_ast(self, antlr4_tree: SmallerBasicParser.ProgramContext) -> Ast:
        """
        Create the AST.

        Args:
            antlr4_tree (SmallerBasicParser.ProgramContext): The ANTLR4 tree.
        """
        if not self.__is_running:
            raise RunningRuntimeError(self.create_ast.__name__, self.__is_running)

        self.print("Create the AST...\n")
        smaller_basic_ast_visitor: SmallerBasicAstVisitor = SmallerBasicAstVisitor()
        smaller_basic_ast: Ast = smaller_basic_ast_visitor.visit(antlr4_tree)

        return smaller_basic_ast

    def print_ast(self, smaller_basic_ast: Ast) -> None:
        """
        Print the AST.

        Args:
            smaller_basic_ast (Ast): The AST.
        """
        if not self.__is_running:
            raise RunningRuntimeError(self.print_ast.__name__, self.__is_running)

        self.print("Print the AST...\n")
        print(smaller_basic_ast)

    def generate_dot_file(self, smaller_basic_ast: Ast, filename: str = "ast") -> None:
        """
        Generate the dot file.

        Args:
            smaller_basic_ast (Ast): The AST.
        """
        if not self.__is_running:
            raise RunningRuntimeError(self.generate_dot_file.__name__, self.__is_running)

        self.print("Generate the dot file...\n")
        smaller_basic_ast.create_dot_files(filename=filename,
                                           generate_png=True,
                                           view="default-viewer")

    def invoke_library_function(self, lib_name: str, func_name: str, *args) -> Any:
        """
        Invoke the library function.
        """
        if not self.__is_running:
            raise RunningRuntimeError(self.invoke_library_function.__name__, self.__is_running)

        if lib_name not in self.__libraries:
            raise NameError(f"Library {lib_name} is not defined.")

        if lib_name == "IO":
            from src.interpreter.library.io import IO
            io: IO = IO()
            res = io.call(func_name, *args)

        return res

    def eval(self, smaller_basic_ast: Ast) -> None:
        """
        Evaluate the AST.
        """
        if not self.__is_running:
            raise RunningRuntimeError(self.eval.__name__, self.__is_running)

        self.print("Evaluate the AST...\n")
        print(f"+----------{len(self.__file_path) * '-'}--------+")
        print(f"| ----- Run {color.set_color_cyan(self.__file_path)} ----- |")
        print(f"+----------{len(self.__file_path) * '-'}--------+")
        print()
        self.global_memory.reset()
        smaller_basic_ast.visit(self)

    def run(self, file_path):
        """
        Run the interpreter.

        Args:
            file_path (str): The path to the source code file.
        """
        self.load_file(file_path)

        if self.__source_code is not None:
            self.__is_running = True
        else:
            raise RunningRuntimeError(self.run.__name__, self.__is_running)

        self.print("Interpreter is running...\n")

        token_stream: CommonTokenStream = self.do_lexical_analysis()
        smaller_basic_tree: SmallerBasicParser.ProgramContext = self.do_parser(token_stream, print_res = False)
        smaller_basic_ast: Ast = self.create_ast(smaller_basic_tree)

        self.print_ast(smaller_basic_ast)
        # self.generate_dot_file(smaller_basic_ast, filename = f"ast-{file_path.split('/')[-1].split('.')[0]}")
        self.eval(smaller_basic_ast)
        self.__is_running = False

    @staticmethod
    def print(string: str):
        print(string)

from src.utils.color_print import apply_color_print
Interpreter = apply_color_print(Interpreter, color.CYAN)

# from src.utils.color_print import *
# Interpreter = ColorPrint(color.CYAN)("Interpreter", (object, ), dict(Interpreter.__dict__))

