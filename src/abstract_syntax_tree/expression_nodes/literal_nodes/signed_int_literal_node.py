from src.abstract_syntax_tree.expression_nodes.abstract_expression_node import AbstractExpressionNode

class SignedIntLiteralNode(AbstractExpressionNode):
    """
    Class representing a signed int literal node in the abstract syntax tree.
    """

    def __init__(self, sign: str, number: str):
        """
        Initialize an instance of SignedNumberLiteralNode.
        """
        super().__init__()
        self.sign: str = sign
        self.number: str = number 
        self.sign_num: int = int(sign + number)
        self.name: str = "SignedIntLiteralNode"
        
    def visit(self): pass
