from typing import List
import os
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

    def str_dot(self) -> str:
        dot_str: str = "digraph Ast {\n"
        dot_str += "\trankdir=TD;\n"
        dot_str += "\tnode [shape=box];\n"

        def traverse(node, parent_id: str):
            node_id: str = str(id(node))
            dot_str: str = f"\t{node_id} [label=\"{node.name}\"];\n"
            if parent_id != "":
                dot_str += f"\t{parent_id} -> {node_id};\n"

            if node.children:
                for child in node.children:
                    dot_str += traverse(child, node_id)

            return dot_str

        dot_str += traverse(self, "")
        dot_str += "}\n"
        return dot_str

    def create_dot_files(self, filename: str = "tree", generate_png: bool = False, view: str = "default-viewer"):
        """
        This function is used to create the dot file for the AST.

        Parameters:
            filename (str): The name of the dot file.
            generate_png (bool): Whether to generate the png file.
            view (str): The viewer to use. ["code", "default-viewer"]
        """
        str_dot: str = self.str_dot()

        os.makedirs("dot_figs", exist_ok=True)
        filename_dot: str = f"dot_figs/{filename}.dot"
        with open(filename_dot, "w") as f:
            f.write(str_dot)

        import subprocess
        if generate_png:
            command: str = f"dot -Tpng dot_figs/{filename}.dot -o dot_figs/{filename}.png"
            subprocess.run(command, shell=True, check=True)
        match view:
            case "code":
                command: str = f"code dot_figs/{filename}.png"
            case "default-viewer":
                command: str = f"nohup xdg-open 'dot_figs/{filename}.png' >/dev/null 2>&1 &"
        subprocess.run(command, shell=True, check=True)

    @abstractmethod
    def visit(self, interpreter):
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

