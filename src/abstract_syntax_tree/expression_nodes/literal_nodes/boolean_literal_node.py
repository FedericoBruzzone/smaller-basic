from src.abstract_syntax_tree.expression_nodes.abstract_expression_node import AbstractExpressionNode

class BooleanLiteralNode(AbstractExpressionNode):
    """
    Class representing a boolean literal node in the abstract syntax tree.
    """
    
    def __init__(self, boolean: str):
        """
        Initialize an instance of BooleanLiteralNode.
        """
        super().__init__()
        self.boolean: bool = self.get_value(boolean) 
        self.name: str = "BooleanLiteralNode"
       
        print(f"BooleanLiteralNode object created with value: {self.boolean}") 

    def get_value(self, boolean: str) -> bool:
        """
        Return the value of the boolean literal.
        """
        if boolean == "true":
            return True
        else:
            return False

    def visit(self): pass
