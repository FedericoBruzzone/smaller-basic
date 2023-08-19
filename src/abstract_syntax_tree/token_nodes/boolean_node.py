from src.abstract_syntax_tree.token_nodes.abstract_token_node import AbstractTokenNode

class BooleanNode(AbstractTokenNode):
    """
    Boolean node class. It represents an boolean.
    """
    def __init__(self, value: str):
        """
        Constructor for BooleanNode class.

        Parameters:
            value (str): The value of the int.
        """

        super().__init__()
        self.value = value 
        self.name = "BooleanNode"

    def visit(self, interpreter) -> bool:
        return self.value == "true"

