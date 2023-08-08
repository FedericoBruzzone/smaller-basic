from typing import Any
from src.abstract_syntax_tree.expression_nodes.logical_boolean_expression_nodes.logical_boolean_expression_node import \
    LogicalBooleanExpressionNode

class LogicalExpressionNode(LogicalBooleanExpressionNode):
    """
    Represents a logical expression
    """

    def __init__(
        self,
        left_expression_node: Any,
        operator: str,
        right_expression_node: Any
    ):
        # accepted_types = [IdNode,
        #                   IntNode,
        #                   FloatNode,
        #                   UnaryAtomNumberNode,
        #                   MultiplicativeExpressionNode]
        # if (type(left_expression_node) not in accepted_types and
        #         not issubclass(type(left_expression_node), ArithmeticalExpressionNode)):
        #     raise ValueError(
        #         f"Left expression node must be of type {accepted_types} or a subclass of ArithmeticalExpressionNode. Got: {type(left_expression_node)}")
        # if operator and operator != '+' and operator != '-':
        #     raise ValueError(
        #         f"Operator {operator} is not supported for additive expressions. Only '+' and '-' are supported.")
        # if (type(right_expression_node) not in accepted_types and
        #         not issubclass(type(right_expression_node), ArithmeticalExpressionNode)):
        #     raise ValueError(
        #         f"Right expression node must be of type {accepted_types} or a subclass of ArithmeticalExpressionNode. Got: {type(right_expression_node)}")

        super().__init__([left_expression_node, right_expression_node])
        self.operator: str = operator
        self.name: str = "LogicalExpressionNode"

    def visit(self): pass
