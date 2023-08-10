from src.abstract_syntax_tree.statement_nodes.abstract_statement_node import AbstractStatementNode

class DeclarationStatementNode(AbstractStatementNode):
    """
    Represents a declaration statement in the abstract syntax tree.
    """

    def __init__(self, children: list = list()):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        super().__init__(children)
        self.name = "DeclarationStatementNode"

