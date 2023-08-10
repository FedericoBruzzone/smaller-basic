from src.abstract_syntax_tree.statement_nodes.if_statement_nodes.if_statement_node import IfStatementNode
from src.abstract_syntax_tree.statement_nodes.statements_node import StatementsNode
from src.abstract_syntax_tree.expression_nodes.logical_boolean_expression_nodes.logical_boolean_expression_node import LogicalBooleanExpressionNode

class IfStatementWithElseNode(IfStatementNode):
    """
    If statement with else node class. It represents an if statement with else in the AST.
    """

    def __init__(self, 
                 condition: LogicalBooleanExpressionNode, 
                 then_body: StatementsNode, 
                 else_body: StatementsNode):
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
        if not isinstance(else_body, StatementsNode):
            raise ValueError(
                f"Else body must be of type StatementsNode. Got: {type(else_body)}")
        
        super().__init__([condition, then_body, else_body])
        self.name = "IfStatementWithElseNode"
