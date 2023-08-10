from typing import Any
from src.abstract_syntax_tree.expression_nodes.logical_boolean_expression_nodes.logical_boolean_expression_node import \
    LogicalBooleanExpressionNode
from src.abstract_syntax_tree.expression_nodes.string_expression_nodes.string_expression_node import StringExpressionNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode
from src.abstract_syntax_tree.token_nodes.string_node import StringNode

class BooleanStringExpressionNode(LogicalBooleanExpressionNode):
    """
    Represents a boolean string expression
    """

    def __init__(
        self,
        left_expression_node: Any,
        operator: str,
        right_expression_node: Any
    ):
        acceted_operators = ['=', '<>', '>=', '<=', '>', '<']
        accepted_types = [IdNode, 
                            StringNode]
        accepted_subtypes = [StringExpressionNode]

        if ((type(left_expression_node) not in accepted_types) and
            not issubclass(type(left_expression_node), tuple(accepted_subtypes))):
            raise ValueError(
                f"Left expression node must be of type {accepted_types} or subclass of {accepted_subtypes}. Got: {type(left_expression_node)}")
        if operator not in acceted_operators:
            raise ValueError(
                f"Operator {operator} is not supported for boolean expressions. Only {acceted_operators} are supported.")
        if ((type(right_expression_node) not in accepted_types) and
            not issubclass(type(right_expression_node), tuple(accepted_subtypes))):
            raise ValueError(
                f"Right expression node must be of type {accepted_types} or subclass of {accepted_subtypes}. Got: {type(right_expression_node)}")

        super().__init__([left_expression_node, right_expression_node])
        self.operator: str = operator
        self.name: str = "BooleanStringExpressionNode"

    def visit(self): pass
