from typing import Any
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.arithmetical_expression_node import ArithmeticalExpressionNode
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.unary_atom_number_node import UnaryAtomNumberNode
from src.abstract_syntax_tree.statement_nodes.library_statement_nodes.library_statement_node import LibraryStatementNode 
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
        accepted_subtypes: list = [ArithmeticalExpressionNode,
                          LibraryStatementNode]
        if (type(left_expression_node) not in accepted_types and
            not issubclass(type(left_expression_node), tuple(accepted_subtypes))):
            raise ValueError(
                f"Left expression node must be of type {accepted_types} or a subclass of {accepted_subtypes}. Got: {type(left_expression_node)}")
        if operator and operator != '*' and operator != '/':
            raise ValueError(
                f"Operator {operator} is not supported for additive expressions. Only '*' and '/' are supported.")
        if (type(right_expression_node) not in accepted_types and
                not issubclass(type(right_expression_node), tuple(accepted_subtypes))):
            raise ValueError(
                f"Right expression node must be of type {accepted_types} or a subclass of {accepted_subtypes}. Got: {type(right_expression_node)}")

        super().__init__([left_expression_node, right_expression_node])
        self.operator: str = operator
        self.name: str = "MultiplicativeExpressionNode"

    def get_left_expression_node(self) -> Any:
        return self.children[0]

    def get_operator(self) -> str:
        return self.operator

    def get_right_expression_node(self) -> Any:
        return self.children[1]

    def visit(self, interpreter):
        left_expression_node = self.get_left_expression_node().visit(interpreter)
        right_expression_node = self.get_right_expression_node().visit(interpreter)
        operator = self.get_operator()
        return interpreter.dispatch_table.apply_binary(self.get_operator(),
                                                       left_expression_node,
                                                       right_expression_node)
