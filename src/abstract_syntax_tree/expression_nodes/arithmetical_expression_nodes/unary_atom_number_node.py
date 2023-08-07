from typing import Any
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.arithmetical_expression_node import ArithmeticalExpressionNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode
from src.abstract_syntax_tree.token_nodes.int_node import IntNode
from src.abstract_syntax_tree.token_nodes.float_node import FloatNode

class UnaryAtomNumberNode(ArithmeticalExpressionNode):
    """
    Represents a number that is either a signed integer, a signed float or a signed id.
    """

    def __init__(
        self,
        sign: str,
        atom_number_node: Any 
    ):
        accepted_types = [IntNode, 
                          FloatNode, 
                          IdNode]
        if (type(atom_number_node) not in accepted_types and 
            not issubclass(type(atom_number_node), ArithmeticalExpressionNode)):
            raise ValueError(                
                f"Left expression node must be of type {accepted_types}. Got: {type(atom_number_node)}")

        super().__init__([atom_number_node])
        self.sign: str = sign
        self.name: str = "UnaryAtomNumberNode"

    def visit(self): pass
