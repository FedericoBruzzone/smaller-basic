from typing import List
from src.abstract_syntax_tree.handle_goto import handle_goto

from src.abstract_syntax_tree.statement_nodes.abstract_statement_node import AbstractStatementNode
from src.abstract_syntax_tree.abstract_ast_node import AbstractAstNode

class Ast(AbstractAstNode):
    def __init__(self, statements: List[AbstractStatementNode]):
        super().__init__(statements)

        for statement in statements:
            if not isinstance(statement, AbstractStatementNode):
                raise TypeError(f"The statement {statement} must be an instance of AbstractStatementNode or one of its subclasses but was {type(statement)}")

        self.name = "Ast"

    @handle_goto
    def visit(self, interpreter):
        interpreter.ast_root = self
        for statement in self.children:
            statement.visit(interpreter)
