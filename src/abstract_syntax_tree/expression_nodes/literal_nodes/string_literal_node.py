from src.abstract_syntax_tree.expression_nodes.abstract_expression_node import AbstractExpressionNode

class StringLiteralNode(AbstractExpressionNode):
    """
    Class representing a string literal node in the abstract syntax tree.
    """

    def __init__(self, string: str):
        """
        Initialize an instance of StringLiteralNode.
        """
        super().__init__()
        self.string: str = str(string) 
        self.name: str = "StringLiteralNode"
        
        print(f"StringLiteralNode object created with value: {self.string}")

    def visit(self): pass
