class GlobalMemory(object):
    """
    Global memory for the interpreter.
    """

    def __init__(self):
        """
        Constructor for GlobalMemory class.
        """
        self.__global_memory = {}

    def get_value_of(self, id_name: str):
        """
        Get the value of the identifier.

        Parameters:
            id_name (str): The name of the identifier.

        Returns:
            object: The value of the identifier.
        """
        if self.is_defined(id_name):
            return self.__global_memory[id_name]
        else:
            raise Exception("Identifier " + id_name + " is not defined")

    def set_value_of_variable(self, id_name: str, value):
        """
        Set the value of the identifier.

        Parameters:
            id_name (str): The name of the identifier.
            value (object): The value of the identifier.
        """
        self.__global_memory[id_name] = value

    def set_value_of_array(self, id_name: str, indexes: list, value):
        """
        Set the value of the identifier.

        Parameters:
            id_name (str): The name of the identifier.
            indexes (list): The indexes of the array.
            value (object): The value of the identifier.
        """
        print("indexes", indexes)

    def is_defined(self, id_name: str) -> bool:
        """
        Check if the identifier is defined.

        Parameters:
            id_name (str): The name of the identifier.

        Returns:
            bool: True if the identifier is defined, False otherwise.
        """
        return id_name in self.__global_memory

    def reset(self):
        """
        Reset the global memory.
        """
        self.__global_memory = {}
