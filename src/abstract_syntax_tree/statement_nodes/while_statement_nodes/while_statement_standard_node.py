from src.abstract_syntax_tree.statement_nodes.while_statement_nodes.while_statement_node import WhileStatementNode
from src.abstract_syntax_tree.statement_nodes.statements_node import StatementsNode
from src.abstract_syntax_tree.expression_nodes.logical_boolean_expression_nodes.logical_boolean_expression_node import LogicalBooleanExpressionNode

class WhileStatementStandardNode(WhileStatementNode):
    """
    While statement standard node class. It represents a while statement in the AST.
    """

    def __init__(self,
                 condition: LogicalBooleanExpressionNode,
                 while_body: StatementsNode):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        if not issubclass(type(condition), LogicalBooleanExpressionNode):
            raise ValueError(
                f"Condition must be of type LogicalBooleanExpressionNode. Got: {type(condition)}")
        if not isinstance(while_body, StatementsNode):
            raise ValueError(
                f"While body must be of type StatementsNode. Got: {type(while_body)}")
        
        super().__init__([condition, while_body])
        self.name = "WhileStatementStandard"

