from typing import List
from src.abstract_syntax_tree.abstract_ast_node import AbstractAstNode

class ExpressionsNode(AbstractAstNode):
    """
    Expressions node class. It represents a list of expressions in the AST.
    """

    def __init__(self, children: List[AbstractAstNode] = list()):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        for child in children:
            if not isinstance(child, AbstractAstNode):
                raise TypeError(f"Children of ExpressionsNode must be of type AbstractAstNode. Got: {type(child)}")
        super().__init__(children)
        self.name = "ExpressionsNode"
    
    def visit(self, interpreter): 
        for child in self.children:
            child.visit(interpreter)

