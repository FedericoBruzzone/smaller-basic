from src.abstract_syntax_tree.handle_goto import handle_goto
from src.abstract_syntax_tree.statement_nodes.while_statement_nodes.while_statement_node import WhileStatementNode
from src.abstract_syntax_tree.statement_nodes.statements_node import StatementsNode
from src.abstract_syntax_tree.expression_nodes.logical_boolean_expression_nodes.logical_boolean_expression_node import LogicalBooleanExpressionNode
from src.abstract_syntax_tree.token_nodes.boolean_node import BooleanNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode

class WhileStatementStandardNode(WhileStatementNode):
    """
    While statement standard node class. It represents a while statement in the AST.
    """

    def __init__(self,
                 condition: LogicalBooleanExpressionNode,
                 while_body: StatementsNode):
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
        if not isinstance(while_body, StatementsNode):
            raise ValueError(
                f"While body must be of type StatementsNode. Got: {type(while_body)}")

        super().__init__([condition, while_body])
        self.name = "WhileStatementStandard"

    def get_condition(self):
        """
        Gets the condition of the while statement.

        Returns:
            LogicalBooleanExpressionNode: The condition of the while statement.
        """
        return self.children[0]

    def get_while_body(self):
        """
        Gets the body of the while statement.

        Returns:
            StatementsNode: The body of the while statement.
        """
        return self.children[1]

    @handle_goto
    def visit(self, interpreter):
        condition = self.get_condition()
        if type(condition.visit(interpreter)) is not bool:
            print(type(condition.visit(interpreter)))
            raise ValueError(
                f"Condition must be of type bool. Got: {type(condition.visit(interpreter))}")
        while_body = self.get_while_body()
        while condition.visit(interpreter):
            while_body.visit(interpreter)

