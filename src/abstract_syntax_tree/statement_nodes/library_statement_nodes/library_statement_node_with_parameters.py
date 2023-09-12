from src.abstract_syntax_tree.expression_nodes.expressions_node import ExpressionsNode
from src.abstract_syntax_tree.expression_nodes.abstract_expression_node import AbstractExpressionNode
from src.abstract_syntax_tree.handle_goto import handle_goto
from src.abstract_syntax_tree.statement_nodes.library_statement_nodes.library_statement_node import LibraryStatementNode
from src.abstract_syntax_tree.token_nodes.abstract_token_node import AbstractTokenNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode

class LibraryStatementWithParametersNode(LibraryStatementNode):
    """
    Class representing a library statement with parameters in the abstract syntax tree.
    """

    def __init__(self, lib_name: IdNode,
                 func_name: IdNode,
                 expression: ExpressionsNode):
        """
        Initialize a VariableDeclarationStatementNode object.
        """
        if not isinstance(lib_name, IdNode):
            raise TypeError(
                "LibraryStatementNode expects an IdNode as the first argument and got " + str(type(lib_name)))
        if not isinstance(func_name, IdNode):
            raise TypeError(
                "LibraryStatementNode expects an IdNode as the second argument and got " + str(type(func_name)))
        if not isinstance(expression, ExpressionsNode):
            raise TypeError(
                "LibraryStatementNode expects an ExpressionsNode as the third argument and got " + str(type(expression)))
        super().__init__([lib_name, func_name, expression])
        self.name: str = "LibraryStatementNode"

    def get_lib_name(self) -> IdNode:
        """
        Get the library name.

        Returns:
            IdNode: The library name.
        """
        return self.children[0]

    def get_func_name(self) -> IdNode:
        """
        Get the function name.

        Returns:
            IdNode: The function name.
        """
        return self.children[1]

    def get_expression(self) -> AbstractExpressionNode:
        """
        Get the expression.

        Returns:
            AbstractExpressionNode: The expression.
        """
        return self.children[2]

    @handle_goto
    def visit(self, interpreter):
        res = interpreter.invoke_library_function(self.get_lib_name().get_id_name(),
                                                  self.get_func_name().get_id_name(),
                                                  *self.get_expression().visit(interpreter))

        return res

