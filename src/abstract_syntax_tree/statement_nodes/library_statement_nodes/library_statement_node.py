from src.abstract_syntax_tree.statement_nodes.abstract_statement_node import AbstractStatementNode

class LibraryStatementNode(AbstractStatementNode):
    """
    Represents a library statement node in the AST.
    """

    def __init__(self, children: list = list()):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        super().__init__(children)
        self.name = "LibraryStatementNode"

