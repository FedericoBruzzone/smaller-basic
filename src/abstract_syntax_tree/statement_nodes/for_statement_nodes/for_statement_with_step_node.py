from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.arithmetical_expression_node import ArithmeticalExpressionNode
from src.abstract_syntax_tree.handle_goto import handle_goto
from src.abstract_syntax_tree.statement_nodes.declaration_statement_nodes.declaration_statement_node import DeclarationStatementNode
from src.abstract_syntax_tree.statement_nodes.for_statement_nodes.for_statement_node import ForStatementNode
from src.abstract_syntax_tree.statement_nodes.statements_node import StatementsNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode
from src.abstract_syntax_tree.token_nodes.int_node import IntNode
from src.abstract_syntax_tree.token_nodes.float_node import FloatNode

class ForStatementWithStepNode(ForStatementNode):
    """
    For statement with step node class. It represents a for statement in the AST.
    """

    def __init__(self,
                 dec_statement: DeclarationStatementNode,
                 to_expression: ArithmeticalExpressionNode,
                 step_expression: ArithmeticalExpressionNode,
                 statements: StatementsNode):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        accepted_types = [IdNode,
                          IntNode,
                          FloatNode,]
        if (not issubclass(type(dec_statement), DeclarationStatementNode)):
            raise ValueError(
                f"Dec statement must be of type DeclarationStatementNode. Got: {type(dec_statement)}")
        if (type(to_expression) not in accepted_types and
            not issubclass(type(to_expression), ArithmeticalExpressionNode)):
            raise ValueError(
                f"To expression must be of type {accepted_types} or a subclass of ArithmeticalExpressionNode. Got: {type(to_expression)}")
        if (type(step_expression) not in accepted_types and
            not issubclass(type(step_expression), ArithmeticalExpressionNode)):
            raise ValueError(
                f"Step expression must be of type {accepted_types} or a subclass of ArithmeticalExpressionNode. Got: {type(step_expression)}")
        if not isinstance(statements, StatementsNode):
            raise ValueError(
                f"Statements must be of type StatementsNode. Got: {type(statements)}")

        super().__init__([dec_statement, to_expression, statements, step_expression])
        self.name = "ForStatementWithStep"

    def get_step_expression(self) -> ArithmeticalExpressionNode:
        """
        Returns the step expression of the for statement.

        Returns:
            ArithmeticalExpressionNode: The step expression of the for statement.
        """
        return self.children[3]

    @handle_goto
    def visit(self, interpreter):
        name = self.get_dec_statement().get_var_name().get_id_name()

        dec_statement = self.get_dec_statement().visit(interpreter)
        from_expression = self.get_dec_statement().get_expression().visit(interpreter)
        to_expression = self.get_to_expression().visit(interpreter) + 1
        statements = self.get_statements()
        step_expression = self.get_step_expression().visit(interpreter)

        if type(from_expression) == int:
            for i in range(from_expression, to_expression, step_expression):
                statements.visit(interpreter)
                interpreter.global_memory.set_value_of_variable(name, i + step_expression)
        else:
            i = from_expression
            while from_expression < to_expression:
                statements.visit(interpreter)
                interpreter.global_memory.set_value_of_variable(name, i + from_expression)
                from_expression += from_expression

