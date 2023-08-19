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

    def WriteLine(self, *args):
        """
        Write a line to stdout.
        """
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
