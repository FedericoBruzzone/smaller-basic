from src.abstract_syntax_tree.token_nodes.abstract_token_node import AbstractTokenNode

class FloatNode(AbstractTokenNode):
    """
    Float node class. It represents a float.
    """
    def __init__(self, value: str):
        """
        Constructor for FloatNode class.

        Parameters:
            value (str): The value of the float.
        """

        super().__init__()
        self.value = value 
        self.name = "FloatNode"

    def visit(self, interpreter):
        """
        Visitor pattern acceptor.
        """
        return float(self.value)
