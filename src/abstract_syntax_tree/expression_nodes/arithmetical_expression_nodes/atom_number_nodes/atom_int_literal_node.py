from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.atom_number_nodes.atom_number_node import AtomNumberNode
from src.abstract_syntax_tree.expression_nodes.literal_nodes.signed_int_literal_node import SignedIntLiteralNode

class AtomIntLiteralNode(AtomNumberNode, SignedIntLiteralNode):
    """
    Class representing an atom integer literal node in the AST. 
    """

    def __init__(self, sign: str, number: str):
        """
        Initialize an instance of AtomStringLiteralNode. 
        """
        SignedIntLiteralNode.__init__(self, sign, number)
        # self.name: str = "AtomStringLiteralNode"

        # print(f"AtomStringLiteralNode object created with value: {self.string}")
