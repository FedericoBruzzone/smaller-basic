from src.abstract_syntax_tree.statement_nodes.subroutine_statement_nodes.call_subroutine_statement_node import \
    CallSubroutineStatementNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode

class CallSubroutineStatementStandardNode(CallSubroutineStatementNode):
    """
    Call subroutine statement standard node class. It represents a call subroutine statement in the AST.
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
        self.name = "CallSubroutineStatementStandard";
