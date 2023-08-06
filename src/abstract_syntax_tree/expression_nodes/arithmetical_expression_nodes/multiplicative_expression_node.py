from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.arithmetical_expression_node import ArithmeticalExpressionNode
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.atom_number_nodes.atom_number_node import AtomNumberNode

class MultiplicativeExpressionNode(ArithmeticalExpressionNode):
    """
    Represents a multiplicative expression.
    """

    def __init__(
        self,
        left_expression_node: AtomNumberNode,
        operator: str,
        right_expression_node: ArithmeticalExpressionNode
    ):
        if not isinstance(left_expression_node, AtomNumberNode):
            raise ValueError(f"Left expression node must be of type AtomNumberNode. Got: {type(left_expression_node)}")
        if operator and operator not in ['*', '/']:
            raise ValueError(f"Operator {operator} is not supported for multiplicative expressions. Only '*' and '/' are supported.")
        if not isinstance(right_expression_node, ArithmeticalExpressionNode):
            raise ValueError(f"Right expression node must be of type ArithmeticalExpressionNode. Got: {type(right_expression_node)}")

        if operator == None and right_expression_node == None:
            super().__init__([left_expression_node])
        else:
            super().__init__([left_expression_node, right_expression_node])
            self.operator: str = operator
        self.name: str = "MultiplicativeExpressionNode"

    def visit(self): pass
