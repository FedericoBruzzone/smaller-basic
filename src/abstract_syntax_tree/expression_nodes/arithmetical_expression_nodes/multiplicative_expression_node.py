from typing import Any
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.arithmetical_expression_node import ArithmeticalExpressionNode
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.unary_atom_number_node import UnaryAtomNumberNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode
from src.abstract_syntax_tree.token_nodes.int_node import IntNode
from src.abstract_syntax_tree.token_nodes.float_node import FloatNode


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
        accepted_types: list = [UnaryAtomNumberNode,
                                IdNode,
                                IntNode,
                                FloatNode]
        if (type(left_expression_node) not in accepted_types and
                not issubclass(type(left_expression_node), ArithmeticalExpressionNode)):
            raise ValueError(
                f"Left expression node must be of type {accepted_types} or a subclass of ArithmeticalExpressionNode. Got: {type(left_expression_node)}")
        if operator and operator != '*' and operator != '/':
            raise ValueError(
                f"Operator {operator} is not supported for additive expressions. Only '*' and '/' are supported.")
        if (type(right_expression_node) not in accepted_types and
                not issubclass(type(right_expression_node), ArithmeticalExpressionNode)):
            raise ValueError(
                f"Right expression node must be of type {accepted_types} or a subclass of ArithmeticalExpressionNode. Got: {type(right_expression_node)}")

        super().__init__([left_expression_node, right_expression_node])
        self.operator: str = operator
        self.name: str = "MultiplicativeExpressionNode"

    def visit(self): pass
