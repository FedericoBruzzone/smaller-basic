from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.arithmetical_expression_node import ArithmeticalExpressionNode
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.multiplicative_expression_node import MultiplicativeExpressionNode

class AdditiveExpressionNode(ArithmeticalExpressionNode):
    """
    Represents an additive expression.
    """

    def __init__(
        self,
        left_expression_node: MultiplicativeExpressionNode,
        operator: str,
        right_expression_node: MultiplicativeExpressionNode
    ):
        if not isinstance(left_expression_node, MultiplicativeExpressionNode): 
            raise ValueError(f"Left expression node must be of type MultiplicativeExpressionNode. Got: {type(left_expression_node)}")
        if operator and operator != '+' and operator != '-':
            raise ValueError(f"Operator {operator} is not supported for additive expressions. Only '+' and '-' are supported.")
        if right_expression_node and not isinstance(right_expression_node, AdditiveExpressionNode):
            raise ValueError(f"Right expression node must be of type AdditiveExpressionNode. Got: {type(right_expression_node)}")
        
        if operator == None and right_expression_node == None:
            super().__init__([left_expression_node])
        else:
            super().__init__([left_expression_node, right_expression_node])
            self.operator: str = operator
        self.name: str = "AdditiveExpressionNode"

    def visit(self): pass

