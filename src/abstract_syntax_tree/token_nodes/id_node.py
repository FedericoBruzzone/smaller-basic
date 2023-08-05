from src.abstract_syntax_tree.token_nodes.abstract_token_node import AbstractTokenNode

class IdNode(AbstractTokenNode):
    """
    Id node class. It represents an identifier.
    """
    def __init__(self, id_name: str):
        """
        Constructor for IdNode class.

        Parameters:
            name (str): The name of the identifier.
        """
        if id_name is None:
            raise Exception("IdName cannot be None")
        if id_name == "":
            raise Exception("IdName cannot be empty")
        if not id_name.isidentifier():
            raise Exception("IdName must be a valid identifier")

        super().__init__()
        self.id_name = id_name 
        self.name = "IdNode"

    def get_symbol(self) -> str:
        """
        Gets the name of the identifier.

        Returns:
            str: The name of the identifier.
        """
        return self.id_name
    
    def visit(self): pass 
