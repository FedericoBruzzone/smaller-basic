RESET = "\033[0m"
RED = "\033[91m"

def set_color_red(string: str) -> str:
    return RED + string + RESET
