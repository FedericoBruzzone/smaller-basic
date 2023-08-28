from src.utils.color_print import color

class IO(object):
    """
    IO class for reading and writing from/to stdin/stdout.
    """

    def __init__(self):
        """
        Initialize IO class.
        """
        pass

    def __convert_dict_to_list(self, input_dict):
        if isinstance(input_dict, dict):
            keys = list(input_dict.keys())
            if len(keys) == 1 and keys[0] == 0:
                return self.__convert_dict_to_list(input_dict[0])
            else:
                return [self.__convert_dict_to_list(input_dict[key]) for key in keys]
        else:
            return input_dict

    def WriteLine(self, *args):
        """
        Write a line to stdout.
        """
        if type(args[0]) == dict:
            converted_list = self.__convert_dict_to_list(args[0])
            print(converted_list)
        else:
            print(*args)

    def ReadLine(self):
        """
        Read a line from stdin.
        """
        try:
            user_input = input(f"{color.COLOR_GREEN}|> {color.COLOR_RESET}")
            # print(color.COLOR_RESET, end="")
        except:
            raise Exception("Error reading from stdin")

        return user_input

    def call(self, func_name: str, *args):
        """
        Call a function with the given arguments and keyword arguments.
        """
        return getattr(self, func_name)(*args)
