class GlobalMemory(object):
    """
    Global memory for the interpreter.
    """

    def __init__(self):
        """
        Constructor for GlobalMemory class.
        """
        self.__global_memory = {}

    def get_default_value(self, type_of_value: type):
        if type_of_value == int:
            return 0
        elif type_of_value == float:
            return 0.0
        elif type_of_value == str:
            return ""
        elif type_of_value == bool:
            return False
        else:
            raise Exception("Type " + str(type_of_value) + " is not supported")

    def get_value_of_variable(self, id_name: str):
        """
        Get the value of the varible identifier.

        Parameters:
            id_name (str): The name of the identifier.

        Returns:
            object: The value of the identifier.
        """
        if self.is_defined(id_name):
            return self.__global_memory[id_name]
        else:
            raise Exception("Identifier " + id_name + " is not defined")

    def get_value_of_array(self, id_name: str, indexes: list):
        """
        Get the value of the varible identifier.

        Parameters:
            id_name (str): The name of the identifier.
            indexes (list): The indexes of the array.

        Returns:
            object: The value of the identifier.
        """
        for index in indexes:
            if index < 0:
                raise Exception("Array index cannot be negative")

        if self.is_defined(id_name):
            array = self.__global_memory[id_name]
            for index in indexes:
                if index not in array:
                    raise Exception("Array index " + str(index) + " is not defined")
                array = array[index]
            return array
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
        for index in indexes:
            if index < 0:
                raise Exception("Array index cannot be negative")

        if not self.is_defined(id_name):
            type_of_value = type(value)
            default_value = self.get_default_value(type_of_value)

            self.__global_memory[id_name] = {}
            array = self.__global_memory[id_name]
            for index in indexes[:-1]:
                for i in range(index):
                    if i not in array:
                        array[i] = default_value
                if index not in array:
                    array[index] = {}
                array = array[index]
            for i in range(indexes[-1]):
                if i not in array:
                    array[i] = default_value
            array[indexes[-1]] = value
        else:
            array = self.__global_memory[id_name]
            for index in indexes[:-1]:
                if index not in array:
                    raise Exception("Array index " + str(index) + " is not defined")
                array = array[index]

            array[indexes[-1]] = value

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
