from src.abstract_syntax_tree.handle_goto import handle_goto
from src.abstract_syntax_tree.token_nodes.id_node import IdNode
from src.abstract_syntax_tree.expression_nodes.expressions_node import ExpressionsNode

class IdArrayNode(IdNode):
    """
    IdArray node class. It represents an identifier.
    """
    def __init__(self, id_name: str, indexes: ExpressionsNode):
        """
        Constructor for IdArrayNode class.

        Parameters:
            name (str): The name of the identifier.
            indexes (ExpressionsNode): The indexes of the array.
        """

        if not isinstance(indexes, ExpressionsNode):
            raise TypeError("VariableDeclarationStatementNode expects an ExpressionsNode as the second argument and got " + str(type(indexes)))

        super().__init__(id_name)
        self.indexes = indexes
        self.name = "IdArrayNode"

    @handle_goto
    def visit(self, interpreter):
        return interpreter.global_memory.get_value_of_array(self.get_id_name(),
                                                            self.indexes.visit(interpreter))

