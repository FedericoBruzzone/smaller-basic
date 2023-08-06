from typing import List
from abc import ABCMeta
from abc import abstractmethod

class AbstractAstNode(object, metaclass=ABCMeta):
    """
    This is the abstract class for all AST nodes.

    This class is meant to be inherited by all AST nodes.
    """
    
    def __init__(self, children: list = list()):
        """
        Constructor for the AbstractAstNode class.

        Parameters:
            children (list): The list of children nodes.
        """
        self.children: list = children
        self.name: str      = "AbstractAstNode"
    
    def get_num_children(self) -> int:
        """
        This function returns the number of children nodes.

        Returns:
            int: The number of children nodes.
        """
        return len(self.children)

    def __ast_repr(self, end: List[bool] = list()):
        """
        This function is used to recursively represent the AST.

        Parameters:
            end (List[int]): The list of flags indicating whether the current node is the last child of its parent.
        """

        pre = ""
        for i in end[:-1]:
            if i: pre += "   "
            else: pre += "│  "
        
        res = pre + ("" if len(end) == 0 else "└──" if end[-1] else "├──") + self.name + '\n'
        
        if self.get_num_children() > 0:
            for child in self.children[:-1]:
                res += child.__ast_repr(end + [False])
            if self.children[-1]:
                res += self.children[-1].__ast_repr(end + [True])

        return res
    
    @abstractmethod
    def visit(self):
        """
        This function is used to visit the current node.
        """
        pass

    @staticmethod
    def print(string: str):
        print(string)

    def __str__(self):
        self.print(self.__ast_repr())
        return "" 

from src.utils.color_print import color
from src.utils.color_print import apply_color_print
AbstractAstNode = apply_color_print(AbstractAstNode, color.MAGENTA)

