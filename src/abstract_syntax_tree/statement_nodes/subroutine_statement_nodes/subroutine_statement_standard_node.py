from src.abstract_syntax_tree.statement_nodes.statements_node import StatementsNode
from src.abstract_syntax_tree.statement_nodes.subroutine_statement_nodes.subroutine_statement_node import \
    SubroutineStatementNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode

class SubroutineStatementStandardNode(SubroutineStatementNode):
    """
    Subroutine statement standard node class. It represents a subroutine statement in the AST.
    """
    
    def __init__(self,
                 id_node: IdNode,
                 subroutine_body: StatementsNode):
        """
        Initializes the node with the given children.

        Parameters:
            children (list): The children of the node.
        """
        if not isinstance(id_node, IdNode):
            raise ValueError(
                f"Id node must be of type IdNode. Got: {type(id_node)}")
        if not isinstance(subroutine_body, StatementsNode):
            raise ValueError(
                f"Subroutine body must be of type StatementsNode. Got: {type(subroutine_body)}")
        
        super().__init__([id_node, subroutine_body])
        self.name = "SubroutineStatementStandard"

