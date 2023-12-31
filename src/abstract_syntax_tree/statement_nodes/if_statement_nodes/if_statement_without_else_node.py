from src.abstract_syntax_tree.handle_goto import handle_goto
from src.abstract_syntax_tree.statement_nodes.if_statement_nodes.if_statement_node import IfStatementNode
from src.abstract_syntax_tree.statement_nodes.statements_node import StatementsNode
from src.abstract_syntax_tree.expression_nodes.logical_boolean_expression_nodes.logical_boolean_expression_node import LogicalBooleanExpressionNode
from src.abstract_syntax_tree.token_nodes.boolean_node import BooleanNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode

class IfStatementWithoutElseNode(IfStatementNode):
    """
    If statement without else node class. It represents an if statement without else in the AST.
    """

    def __init__(self,
                 condition: LogicalBooleanExpressionNode,
                 then_body: StatementsNode):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        accepted_types = [BooleanNode,
                          IdNode]
        if (type(condition) not in accepted_types and
            not issubclass(type(condition), LogicalBooleanExpressionNode)):
            raise ValueError(
                f"Condition must be of type LogicalBooleanExpressionNode or {accepted_types}. Got: {type(condition)}")
        if not isinstance(then_body, StatementsNode):
            raise ValueError(
                f"If body must be of type StatementsNode. Got: {type(then_body)}")

        super().__init__([condition, then_body])
        self.name = "IfStatementWithoutElseNode"

    def get_condition(self) -> LogicalBooleanExpressionNode:
        """
        Get the condition of the if statement.

        Returns:
            LogicalBooleanExpressionNode: The condition of the if statement.
        """
        return self.children[0]

    def get_then_body(self) -> StatementsNode:
        """
        Get the then body of the if statement.

        Returns:
            StatementsNode: The then body of the if statement.
        """
        return self.children[1]

    @handle_goto
    def visit(self, interpreter):
        condition = self.get_condition().visit(interpreter)
        if type(condition) is not bool:
            raise ValueError(
                f"Condition must be of type bool. Got: {type(condition)}")
        if condition:
            self.get_then_body().visit(interpreter)

