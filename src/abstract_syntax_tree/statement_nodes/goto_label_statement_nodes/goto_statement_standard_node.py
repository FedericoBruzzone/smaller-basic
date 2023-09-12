from src.abstract_syntax_tree.handle_goto import handle_goto
from src.abstract_syntax_tree.statement_nodes.goto_label_statement_nodes.goto_statement_node import GotoStatementNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode

class GotoStatementStandardNode(GotoStatementNode):
    """
    Goto statement standard node class. It represents a goto statement in the AST.
    """

    def __init__(self,
                 id_node: IdNode):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        if not isinstance(id_node, IdNode):
            raise ValueError(
                f"Id node must be of type IdNode. Got: {type(id_node)}")

        super().__init__([id_node])
        self.name = "GotoStatementStandard"

    def get_id_node(self):
        """
        Returns the id node of the goto statement.

        Returns:
            IdNode: The id node of the goto statement.
        """
        return self.children[0]

    def visit(self, interpreter):
        interpreter.goto_mode = True
        interpreter.goto_label = self.get_id_node().get_id_name()
        interpreter.ast_root.visit(interpreter)
