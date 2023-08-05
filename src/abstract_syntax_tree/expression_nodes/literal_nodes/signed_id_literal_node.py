from src.abstract_syntax_tree.expression_nodes.abstract_expression_node import AbstractExpressionNode

class SignedIdLiteralNode(AbstractExpressionNode):
    """
    Class representing a signed id literal node in the abstract syntax tree.
    """

    def __init__(self, sign: str, id_name: str):
        """
        Initialize an instance of SignedIdLiteralNode.
        """
        super().__init__()
        self.sign: str = sign
        self.id_name: str = id_name
        self.name: str = "SignedIdLiteralNode" 
        
        print(f"SignedIdLiteralNode object created with value: {self.sign}{self.id_name}")

    def visit(self): pass
