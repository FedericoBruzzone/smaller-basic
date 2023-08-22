from typing import Any
from src.abstract_syntax_tree.statement_nodes.library_statement_nodes.library_statement_node import LibraryStatementNode 
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
        accepted_types = [IdNode,
                          IntNode,
                          FloatNode, 
                          IdNode]
        accepted_subtypes = [ArithmeticalExpressionNode,
                LibraryStatementNode]
        if ((type(atom_number_node) not in accepted_types) and 
            not issubclass(type(atom_number_node), tuple(accepted_subtypes))):
            raise ValueError(
                f"Right expression node must be of type {accepted_types} or a subclass of {accepted_subtypes}. Got: {type(atom_number_node)}")
        super().__init__([atom_number_node])
        self.sign: str = sign
        self.name: str = "UnaryAtomNumberNode"

    def get_atom_number_node(self) -> Any:
        return self.children[0]

    def get_sign(self) -> str:
        return self.sign

    def visit(self, interpreter):
        atom_number_node = self.get_atom_number_node().visit(interpreter)
        return interpreter.dispatch_table.apply_unary(self.get_sign(), atom_number_node)
        
