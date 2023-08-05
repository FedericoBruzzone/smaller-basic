from src.abstract_syntax_tree.expression_nodes.abstract_expression_node import AbstractExpressionNode

class StringExpressionNode(AbstractExpressionNode):
    """
    String expression node class. 
    """

    def __init__(self, children: list = list()):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        super().__init__(children)
        self.name = "StringExpressionNode"

