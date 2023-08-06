from src.abstract_syntax_tree.expression_nodes.string_expression_nodes.string_expression_node import StringExpressionNode
from src.abstract_syntax_tree.expression_nodes.string_expression_nodes.atom_string_nodes.atom_string_node import AtomStringNode

class AdditiveStringExpressionNode(StringExpressionNode):
    """
    Represents an additive string expression.
    """

    def __init__(
        self,
        left_string_expression_node: AtomStringNode,
        operator: str,
        right_string_expression_node: StringExpressionNode
    ):
        if not isinstance(left_string_expression_node, AtomStringNode):
            raise ValueError(f"Left string expression node must be of type AtomStringNode. Got: {type(left_string_expression_node)}")
        if operator and operator != '+':
            raise ValueError(f"Operator {operator} is not supported for string expressions. Only '+' is supported.")
        if right_string_expression_node and  not isinstance(right_string_expression_node, StringExpressionNode):
            raise ValueError(f"Right string expression node must be of type StringExpressionNode. Got: {type(right_string_expression_node)}")

        super().__init__([left_string_expression_node, right_string_expression_node])
        self.operator: str = operator
        self.name: str = "AdditiveStringExpressionNode"

        print(f"AdditiveStringExpressionNode object created with: {left_string_expression_node}, {self.operator}, {right_string_expression_node}")

    def visit(self): pass
