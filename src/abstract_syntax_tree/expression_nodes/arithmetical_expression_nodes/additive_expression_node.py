from typing import Any
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.arithmetical_expression_node import ArithmeticalExpressionNode
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.multiplicative_expression_node import MultiplicativeExpressionNode
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.unary_atom_number_node import UnaryAtomNumberNode
from src.abstract_syntax_tree.statement_nodes.library_statement_nodes.library_statement_node import LibraryStatementNode 
from src.abstract_syntax_tree.token_nodes.id_node import IdNode
from src.abstract_syntax_tree.token_nodes.int_node import IntNode
from src.abstract_syntax_tree.token_nodes.float_node import FloatNode


class AdditiveExpressionNode(ArithmeticalExpressionNode):
    """
    Represents an additive expression.
    """

    def __init__(
        self,
        left_expression_node: Any,
        operator: str,
        right_expression_node: Any
    ):
        accepted_types = [IdNode,
                          IntNode,
                          FloatNode,
                          UnaryAtomNumberNode,
                          MultiplicativeExpressionNode]
        accepted_subtypes: list = [ArithmeticalExpressionNode,
                          LibraryStatementNode]
        if (type(left_expression_node) not in accepted_types and
            not issubclass(type(left_expression_node), tuple(accepted_subtypes))):
            raise ValueError(
                f"Left expression node must be of type {accepted_types} or a subclass of ArithmeticalExpressionNode. Got: {type(left_expression_node)}")
        if operator and operator != '+' and operator != '-':
            raise ValueError(
                f"Operator {operator} is not supported for additive expressions. Only '+' and '-' are supported.")
        if (type(right_expression_node) not in accepted_types and
                not issubclass(type(right_expression_node), tuple(accepted_subtypes))):
            raise ValueError(
                f"Right expression node must be of type {accepted_types} or a subclass of {accepted_subtypes}. Got: {type(right_expression_node)}")

        super().__init__([left_expression_node, right_expression_node])
        self.operator: str = operator
        self.name: str = "AdditiveExpressionNode"

    def visit(self): pass
