from src.abstract_syntax_tree.handle_goto import handle_goto
from src.abstract_syntax_tree.token_nodes.abstract_token_node import AbstractTokenNode

class StringNode(AbstractTokenNode):
    """
    String node class. It represents a string.
    """

    def __init__(self, string: str):
        """
        Initialize an instance of StringNode.
        """
        super().__init__()
        self.string: str = str(string)
        self.name: str = "StringNode"

    @handle_goto
    def visit(self, interpreter):
        """
        Visitor pattern acceptor.
        """
        return str(self.string)
