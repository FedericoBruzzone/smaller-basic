from typing import Any
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.arithmetical_expression_node import ArithmeticalExpressionNode
from src.abstract_syntax_tree.expression_nodes.literal_nodes.signed_int_literal_node import SignedIntLiteralNode
from src.abstract_syntax_tree.expression_nodes.literal_nodes.signed_float_literal_node import SignedFloatLiteralNode
from src.abstract_syntax_tree.expression_nodes.literal_nodes.signed_id_literal_node import SignedIdLiteralNode

class MultiplicativeExpressionNode(ArithmeticalExpressionNode):
    """
    Represents a multiplicative expression.
    """

    def __init__(
        self,
        left_expression_node: Any,
        operator: str,
        right_expression_node: ArithmeticalExpressionNode
    ):
        accepted_types: list = [SignedIntLiteralNode, 
                                SignedFloatLiteralNode,
                                SignedIdLiteralNode]
        if type(left_expression_node) not in accepted_types and not issubclass(type(left_expression_node), ArithmeticalExpressionNode): 
            raise ValueError(f"Left expression node must be of type {accepted_types}. Got: {type(left_expression_node)}")
        if operator and operator not in ['*', '/']:
            raise ValueError(f"Operator {operator} is not supported for multiplicative expressions. Only '*' and '/' are supported.")
        if right_expression_node and not isinstance(right_expression_node, ArithmeticalExpressionNode):
            raise ValueError(f"Right expression node must be of type ArithmeticalExpressionNode. Got: {type(right_expression_node)}")

        if operator == None and right_expression_node == None:
            super().__init__([left_expression_node])
        else:
            super().__init__([left_expression_node, right_expression_node])
            self.operator: str = operator
        self.name: str = "MultiplicativeExpressionNode"

    def visit(self): pass
