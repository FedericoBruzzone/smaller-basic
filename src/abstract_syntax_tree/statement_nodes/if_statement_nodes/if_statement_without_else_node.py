from src.abstract_syntax_tree.statement_nodes.if_statement_nodes.if_statement_node import IfStatementNode
from src.abstract_syntax_tree.statement_nodes.statements_node import StatementsNode
from src.abstract_syntax_tree.expression_nodes.logical_boolean_expression_nodes.logical_boolean_expression_node import LogicalBooleanExpressionNode

class IfStatementWithoutElseNode(IfStatementNode):
    """
    If statement without else node class. It represents an if statement without else in the AST.
    """

    def __init__(self, 
                 condition: LogicalBooleanExpressionNode, 
                 then_body: StatementsNode):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        if not issubclass(type(condition), LogicalBooleanExpressionNode):
            raise ValueError(
                f"Condition must be of type LogicalBooleanExpressionNode. Got: {type(condition)}")
        if not isinstance(then_body, StatementsNode):
            raise ValueError(
                f"If body must be of type StatementsNode. Got: {type(then_body)}")
        
        super().__init__([condition, then_body])
        self.name = "IfStatementWithoutElseNode"

