from typing import Any
from src.abstract_syntax_tree.expression_nodes.string_expression_nodes.string_expression_node import StringExpressionNode
from src.abstract_syntax_tree.expression_nodes.literal_nodes.string_literal_node import StringLiteralNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode

class AdditiveStringExpressionNode(StringExpressionNode):
    """
    Represents an additive string expression.
    """

    def __init__(
        self,
        left_string_expression_node: Any,
        operator: str,
        right_string_expression_node: StringExpressionNode
    ):
        if type(left_string_expression_node) not in [StringLiteralNode, IdNode]:
            raise ValueError(f"Left string expression node must be of type StringLiteralNode or IdNode. Got: {type(left_string_expression_node)}") 
        if operator and operator != '+':
            raise ValueError(f"Operator {operator} is not supported for string expressions. Only '+' is supported.")
        if right_string_expression_node and  not isinstance(right_string_expression_node, StringExpressionNode):
            raise ValueError(f"Right string expression node must be of type StringExpressionNode. Got: {type(right_string_expression_node)}")
        
        if operator == None and right_string_expression_node == None:
            super().__init__([left_string_expression_node])
        else:
            super().__init__([left_string_expression_node, right_string_expression_node])
            self.operator: str = operator
        self.name: str = "AdditiveStringExpressionNode"

    def visit(self): pass
