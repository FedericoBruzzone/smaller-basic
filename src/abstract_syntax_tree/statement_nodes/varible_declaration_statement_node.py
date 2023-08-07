from src.abstract_syntax_tree.statement_nodes.abstract_statement_node import AbstractStatementNode
from src.abstract_syntax_tree.expression_nodes.abstract_expression_node import AbstractExpressionNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode

class VariableDeclarationStatementNode(AbstractStatementNode):
    """
    Class representing a declaration statement in the abstract syntax tree.
    """

    def __init__(self, var_name: IdNode, expression: AbstractExpressionNode):
        """
        Initialize a VariableDeclarationStatementNode object.
        """
        # if not isinstance(var_name, IdNode):
        #     raise TypeError("VariableDeclarationStatementNode expects an IdNode as the first argument and got " + str(type(var_name)))
        # if not isinstance(expression, AbstractExpressionNode):
        #     raise TypeError("VariableDeclarationStatementNode expects an AbstractExpressionNode as the second argument and got " + str(type(expression)))
        super().__init__([var_name, expression])
        self.name: str = "VariableDeclarationStatementNode"

    def get_var_name(self) -> IdNode:
        """
        Get the variable name.

        Returns:
            IdNode: The variable name.
        """
        return self.children[0]

    def get_expression(self) -> AbstractExpressionNode:
        """
        Get the expression.
        
        Returns:
            AbstractExpressionNode: The expression.
        """
        return self.children[1]
    
    def visit(self): pass
    
