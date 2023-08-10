from typing import List
from src.abstract_syntax_tree.abstract_ast_node import AbstractAstNode

class StatementsNode(AbstractAstNode):
    """
    Statement node class. It represents a list of statement in the AST.
    """

    def __init__(self, children: List[AbstractAstNode] = list()):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        for child in children:
            if not isinstance(child, AbstractAstNode):
                raise TypeError(f"Children of StatementsNode must be of type AbstractAstNode. Got: {type(child)}")
        super().__init__(children)
        self.name = "StatementsNode"
    
    def visit(self): 
        """
        Visit each child of the node.
        """
        for child in self.children:
            child.visit()

