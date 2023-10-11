import copy


class GlobalMemory(object):
    """
    Global memory for the interpreter.
    """

    def __init__(self):
        """
        Constructor for GlobalMemory class.
        """
        self.__global_memory = {}
        self.__global_functions = {}
        self.__labels = {}

    def get_default_value(self, type_of_value: type):
        """
        Get the default value for the given type.

        Parameters:
            type_of_value (type): The type of the value.
        """
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

        for i in range(len(indexes)):
            indexes[i] = indexes[i] - 1

        if self.is_defined(id_name):
            array = self.__global_memory[id_name]
            if type(array) != list:
                raise Exception("Identifier " + id_name + " is not an array")
            for index in indexes:
                if index not in set(range(len(array))):
                    raise Exception("Array index " + str(index) + " is not defined")
                array = array[index]
            return array
        else:
            raise Exception("Identifier " + id_name + " is not defined")

    def get_body_of_function(self, id_name: str):
        """
        Get the body of the function.

        Parameters:
            id_name (str): The name of the identifier.

        Returns:
            object: The body of the function.
        """
        if self.is_function_defined(id_name):
            return self.__global_functions[id_name]
        else:
            raise Exception("Function " + id_name + " is not defined")

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

            array = [default_value for _ in range(indexes[-1] + 1)]
            for index in reversed(indexes[:-1]):
                array = [copy.deepcopy(array) for _ in range(index + 1)]

            tmp = array
            for index in indexes[:-1]:
                tmp = tmp[index]
            tmp[indexes[-1]] = value

            self.__global_memory[id_name] = array
        else:
            for i in range(len(indexes)):
                indexes[i] = indexes[i] - 1
            array = self.__global_memory[id_name]
            for index in indexes[:-1]:
                array = array[index]
            array[indexes[-1]] = value

    def set_body_of_function(self, id_name: str, body):
        """
        Set the body of the function.

        Parameters:
            id_name (str): The name of the identifier.
            body (object): The body of the function.
        """
        self.__global_functions[id_name] = body

    def add_label(self, id_name: str, label):
        """
        Add a label.

        Parameters:
            id_name (str): The name of the identifier.
            label (object): The label.
        """
        if self.is_label_defined(id_name):
            raise Exception("Label " + id_name + " is already defined")
        self.__labels[id_name] = label

    def is_defined(self, id_name: str) -> bool:
        """
        Check if the identifier is defined.

        Parameters:
            id_name (str): The name of the identifier.

        Returns:
            bool: True if the identifier is defined, False otherwise.
        """
        return id_name in self.__global_memory

    def is_function_defined(self, id_name: str) -> bool:
        """
        Check if the function is defined.

        Parameters:
            id_name (str): The name of the function.

        Returns:
            bool: True if the function is defined, False otherwise.
        """
        return id_name in self.__global_functions

    def is_label_defined(self, id_name: str) -> bool:
        """
        Check if the label is defined.

        Parameters:
            id_name (str): The name of the label.

        Returns:
            bool: True if the label is defined, False otherwise.
        """
        return id_name in self.__labels

    def reset(self):
        """
        Reset the global memory.
        """
        self.__global_memory = {}
        self.__global_functions = {}
        self.__labels = {}
