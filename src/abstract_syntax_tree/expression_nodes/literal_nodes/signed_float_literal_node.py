from src.abstract_syntax_tree.expression_nodes.abstract_expression_node import AbstractExpressionNode

class SignedFloatLiteralNode(AbstractExpressionNode):
    """
    Class representing a signed float literal node in the abstract syntax tree.
    """

    def __init__(self, sign: str, number: str):
        """
        Initialize an instance of SignedFloatLiteralNode.
        """
        super().__init__()
        self.sign: str = sign
        self.number: str = number 
        self.sign_float: float = float(sign + number)
        self.name: str = "SignedFloatLiteralNode"
        
        print(f"SignedFloatLiteralNode object created with value: {str(self.sign_float)}")

    def visit(self): pass
