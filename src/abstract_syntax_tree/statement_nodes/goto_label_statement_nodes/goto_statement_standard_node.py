from src.abstract_syntax_tree.statement_nodes.goto_label_statement_nodes.goto_statement_node import GotoStatementNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode

class GotoStatementStandardNode(GotoStatementNode):
    """
    Goto statement standard node class. It represents a goto statement in the AST.
    """
    
    def __init__(self,
                 id_node: IdNode):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        if not isinstance(id_node, IdNode):
            raise ValueError(
                f"Id node must be of type IdNode. Got: {type(id_node)}")
        
        super().__init__([id_node])
        self.name = "GotoStatementStandard"

