from typing import Any
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

    def get_left_expression_node(self) -> Any:
        """
        Get the left expression node.

        Returns:
            Any: The left expression node.
        """
        return self.children[0]

        
    def get_right_expression_node(self) -> Any:
        """
        Get the right expression node.

        Returns:
            Any: The right expression node.
        """
        return self.children[1]


