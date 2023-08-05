from src.abstract_syntax_tree.expression_nodes.string_expression_nodes.string_expression_node import StringExpressionNode

class AdditiveStringExpressionNodeWithOp(StringExpressionNode):
    """
    Represents an additive string expression with an operator.
    """

    def __init__(
        self,
        left_string_expression_node: StringExpressionNode,
        operator: str,
        right_string_expression_node: StringExpressionNode
    ):
        if operator != '+':
            raise ValueError(f"Operator {operator} is not supported for string expressions. Only '+' is supported.")
        if not isinstance(left_string_expression_node, StringExpressionNode):
            raise ValueError(f"Left string expression node must be of type StringExpressionNode. Got: {left_string_expression_node}")
        if not isinstance(right_string_expression_node, StringExpressionNode):
            raise ValueError(f"Right string expression node must be of type StringExpressionNode. Got: {right_string_expression_node}")

        # operation node 
