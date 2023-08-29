from src.abstract_syntax_tree.statement_nodes.abstract_statement_node import AbstractStatementNode
from src.abstract_syntax_tree.statement_nodes.declaration_statement_nodes.declaration_statement_node import DeclarationStatementNode
from src.abstract_syntax_tree.statement_nodes.statements_node import StatementsNode
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.arithmetical_expression_node import ArithmeticalExpressionNode

class ForStatementNode(AbstractStatementNode):
    """
    Represents an for statement in the abstract syntax tree.
    """

    def __init__(self, children: list = list()):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        super().__init__(children)
        self.name = "ForStatementNode"

    def get_dec_statement(self) -> DeclarationStatementNode:
        """
        Returns the declaration statement of the for statement.

        Returns:
            DeclarationStatementNode: The declaration statement of the for statement.
        """
        return self.children[0]

    def get_to_expression(self) -> ArithmeticalExpressionNode:
        """
        Returns the to expression of the for statement.

        Returns:
            ArithmeticalExpressionNode: The to expression of the for statement.
        """
        return self.children[1]

    def get_statements(self) -> StatementsNode:
        """
        Returns the statements of the for statement.

        Returns:
            StatementsNode: The statements of the for statement.
        """
        return self.children[2]
