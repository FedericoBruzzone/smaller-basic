from src.abstract_syntax_tree.expression_nodes.string_expression_nodes.atom_string_nodes.atom_string_node import AtomStringNode
from src.abstract_syntax_tree.expression_nodes.literal_nodes.string_literal_node import StringLiteralNode

class AtomStringLiteralNode(AtomStringNode, StringLiteralNode):
    """
    Class representing an atom string literal node in the AST.
    """

    def __init__(self, string: str):
        """
        Initialize an instance of AtomStringLiteralNode. 
        """
        StringLiteralNode.__init__(self, string)
        self.string: str = str(string) 
        self.name: str = "AtomStringLiteralNode"

        print(f"AtomStringLiteralNode object created with value: {self.string}")
