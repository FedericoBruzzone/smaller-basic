from src.abstract_syntax_tree.expression_nodes.abstract_expression_node import AbstractExpressionNode
from src.abstract_syntax_tree.statement_nodes.declaration_statement_nodes.declaration_statement_node import DeclarationStatementNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode
from src.abstract_syntax_tree.token_nodes.abstract_token_node import AbstractTokenNode
from src.abstract_syntax_tree.statement_nodes.library_statement_nodes.library_statement_node import LibraryStatementNode
from src.abstract_syntax_tree.expression_nodes.expressions_node import ExpressionsNode

class ArrayDeclarationStatementNode(DeclarationStatementNode):
    """
    Class representing a declaration statement in the abstract syntax tree.
    """

    def __init__(self, var_name: IdNode, indexes: ExpressionsNode, expression: AbstractExpressionNode) -> None:
        """
        Initialize a VariableDeclarationStatementNode object.
        """
        if not isinstance(var_name, IdNode):
            raise TypeError("VariableDeclarationStatementNode expects an IdNode as the first argument and got " + str(type(var_name)))
        if not isinstance(indexes, ExpressionsNode):
            raise TypeError("VariableDeclarationStatementNode expects an ExpressionsNode as the second argument and got " + str(type(indexes)))
        if (not isinstance(expression, AbstractExpressionNode) and 
            not isinstance(expression, AbstractTokenNode) and
            not isinstance(expression, LibraryStatementNode)):
            raise TypeError("VariableDeclarationStatementNode expects an AbstractExpressionNode, AbstractTokenNode or LibraryStatementNode as the second argument and got " + str(type(expression)))
        super().__init__([var_name, indexes, expression])
        self.name: str = "ArrayDeclarationStatementNode"
