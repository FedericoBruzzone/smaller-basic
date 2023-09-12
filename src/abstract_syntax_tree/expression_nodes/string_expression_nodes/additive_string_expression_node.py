from typing import Any
from src.abstract_syntax_tree.expression_nodes.string_expression_nodes.string_expression_node import StringExpressionNode
from src.abstract_syntax_tree.handle_goto import handle_goto
from src.abstract_syntax_tree.token_nodes.string_node import StringNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode
from src.abstract_syntax_tree.statement_nodes.library_statement_nodes.library_statement_node import LibraryStatementNode

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
            not issubclass(type(right_string_expression_node), AdditiveStringExpressionNode)
            and not issubclass(type(right_string_expression_node), LibraryStatementNode)):
            raise ValueError(f"Right string expression node must be of type {accepted_types} or a subclass of AdditiveStringExpressionNode. Got: {type(right_string_expression_node)}")

        super().__init__([left_string_expression_node, right_string_expression_node])
        self.operator: str = operator
        self.name: str = "AdditiveStringExpressionNode"

    def get_operator(self) -> str:
        """
        Get the operator.

        Returns:
            str: The operator.
        """
        return self.operator

    @handle_goto
    def visit(self, interpreter):
        left_expression_node = self.get_left_expression_node().visit(interpreter)
        right_expression_node = self.get_right_expression_node().visit(interpreter)
        return interpreter.dispatch_table.apply_binary(self.get_operator(),
                                                       left_expression_node,
                                                       right_expression_node)

