from src.abstract_syntax_tree.token_nodes.abstract_token_node import AbstractTokenNode

class IntNode(AbstractTokenNode):
    """
    Int node class. It represents an int.
    """
    def __init__(self, value: str):
        """
        Constructor for IntNode class.

        Parameters:
            value (str): The value of the int.
        """

        super().__init__()
        self.value = value 
        self.name = "IntNode"

    def visit(self): pass 
