from src.abstract_syntax_tree.token_nodes.id_node import IdNode
from src.abstract_syntax_tree.statement_nodes.library_statement_nodes.library_statement_node import LibraryStatementNode

class LibraryStatementWithoutParametersNode(LibraryStatementNode):
    """
    Class representing a library statement without parameters in the abstract syntax tree.
    """

    def __init__(self, lib_name: IdNode,
                 func_name: IdNode):
        """
        Initialize a VariableDeclarationStatementNode object.
        """
        if not isinstance(lib_name, IdNode):
            raise TypeError(
                "LibraryStatementWithoutParametersNode expects an IdNode as the first argument and got " + str(type(lib_name)))
        if not isinstance(func_name, IdNode):
            raise TypeError(
                "LibraryStatementWithoutParametersNode expects an IdNode as the second argument and got " + str(type(func_name)))
        super().__init__([lib_name, func_name])
        self.name: str = "LibraryStatementWithoutParametersNode"

    def get_lib_name(self) -> IdNode:
        """
        Get the library name.

        Returns:
            IdNode: The library name.
        """
        return self.children[0]

    def get_func_name(self) -> IdNode:
        """
        Get the function name.

        Returns:
            IdNode: The function name.
        """
        return self.children[1]

    def visit(self, interpreter):
        res = interpreter.invoke_library_function(self.get_lib_name().get_id_name(), 
                                                       self.get_func_name().get_id_name())
        return res
