from src.abstract_syntax_tree.abstract_ast_node import AbstractAstNode

class AbstractExpressionNode(AbstractAstNode):
    """
    Abstract expression node class. 
    """

    def __init__(self, children: list = list()):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        super().__init__(children)
        self.name = "AbstractExpressionNode"

