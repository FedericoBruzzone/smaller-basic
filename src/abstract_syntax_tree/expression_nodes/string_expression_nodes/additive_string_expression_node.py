from typing import Any
from src.abstract_syntax_tree.expression_nodes.string_expression_nodes.string_expression_node import StringExpressionNode
from src.abstract_syntax_tree.token_nodes.string_node import StringNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode

class AdditiveStringExpressionNode(StringExpressionNode):
    """
    Represents an additive string expression.
    """

    def __init__(
        self,
        left_string_expression_node: Any,
        operator: str,
        right_string_expression_node: Any
    ):
        accepted_types: list = [StringNode, 
                                IdNode] 
        if type(left_string_expression_node) not in accepted_types:
            raise ValueError(f"Left string expression node must be of type {accepted_types}. Got: {type(left_string_expression_node)}") 
        if operator and operator != '+':
            raise ValueError(f"Operator {operator} is not supported for string expressions. Only '+' is supported.")
        if (type(right_string_expression_node) not in accepted_types and 
            not issubclass(type(right_string_expression_node), AdditiveStringExpressionNode)):
            raise ValueError(f"Right string expression node must be of type {accepted_types} or a subclass of AdditiveStringExpressionNode. Got: {type(right_string_expression_node)}")
        
        super().__init__([left_string_expression_node, right_string_expression_node])
        self.operator: str = operator
        self.name: str = "AdditiveStringExpressionNode"

    def visit(self): pass
