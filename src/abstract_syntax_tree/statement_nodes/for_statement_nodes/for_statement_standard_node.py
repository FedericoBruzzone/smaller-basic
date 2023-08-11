from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.arithmetical_expression_node import ArithmeticalExpressionNode
from src.abstract_syntax_tree.statement_nodes.declaration_statement_nodes.declaration_statement_node import DeclarationStatementNode
from src.abstract_syntax_tree.statement_nodes.for_statement_nodes.for_statement_node import ForStatementNode
from src.abstract_syntax_tree.statement_nodes.statements_node import StatementsNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode
from src.abstract_syntax_tree.token_nodes.int_node import IntNode

class ForStatementStandardNode(ForStatementNode):
    """
    For statement standard node class. It represents a for statement in the AST.
    """
    
    def __init__(self, 
                 dec_statement: DeclarationStatementNode,
                 to_expression: ArithmeticalExpressionNode,
                 statements: StatementsNode):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        accepted_types = [IdNode,
                               IntNode]
        if (not issubclass(type(dec_statement), DeclarationStatementNode)):
            raise ValueError(
                f"Dec statement must be of type DeclarationStatementNode. Got: {type(dec_statement)}")
        if (type(to_expression) not in accepted_types and
            not issubclass(type(to_expression), ArithmeticalExpressionNode)):
            raise ValueError(
                f"To expression must be of type {accepted_types} or a subclass of ArithmeticalExpressionNode. Got: {type(to_expression)}")
        if not isinstance(statements, StatementsNode):
            raise ValueError(
                f"Statements must be of type StatementsNode. Got: {type(statements)}")
        
        super().__init__([dec_statement, to_expression, statements])
        self.name = "ForStatementStandard"

