from src.abstract_syntax_tree.handle_goto import handle_goto
from src.abstract_syntax_tree.statement_nodes.goto_label_statement_nodes.label_statement_node import LabelStatementNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode

class LabelStatementStandardNode(LabelStatementNode):
    """
    Label statement standard node class. It represents a label statement in the AST.
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
        self.name = "LabelStatementStandardNode"
        self.visited = False

    def get_id_node(self):
        """
        Returns the id node of the label statement.

        Returns:
            IdNode: The id node of the label statement.
        """
        return self.children[0]

    @handle_goto
    def visit(self, interpreter):
        # Check if is the first time visiting the node
        if not self.visited:
            # Add the label to the global memory
            id_name = self.get_id_node().get_id_name()
            interpreter.global_memory.add_label(id_name, self)
            self.visited = True

