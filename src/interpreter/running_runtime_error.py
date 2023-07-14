from src.utils import color

class RunningRuntimeError(RuntimeError):
    def __init__(self, method_name: str, is_running: bool):
        self.__method_name: str = method_name
        self.__is_running: bool = is_running

    def __str__(self):
        string: str = f"\n [ERROR] Interpreter: The method {self.__method_name} cannot be called while the interpreter is" + ("" if self.__is_running else "not") + " running."
        return color.set_color_red(string)
