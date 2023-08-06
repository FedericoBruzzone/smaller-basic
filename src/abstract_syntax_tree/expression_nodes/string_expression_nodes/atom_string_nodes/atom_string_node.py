from src.abstract_syntax_tree.abstract_ast_node import AbstractAstNode

class AtomStringNode(AbstractAstNode): 
    """
    Class representing an atom string node in the AST.
    """

    def __init__(self, children: list = list()):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        super().__init__(children)
        self.name = "AtomStringNode"

    
