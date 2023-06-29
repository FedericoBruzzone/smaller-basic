RESET = "reset"
RED = "red"
GREEN = "green"
YELLOW = "yellow"
BLUE = "blue"
MAGENTA = "magenta"
CYAN = "cyan"
WHITE = "white"
BLACK = "black"

COLOR_RESET = "\033[0m"
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_MAGENTA = "\033[95m"
COLOR_CYAN = "\033[96m"
COLOR_WHITE = "\033[97m"
COLOR_BLACK = "\033[98m"

def set_color_reset(string: str) -> str:
    return COLOR_RESET + string + COLOR_RESET

def set_color_red(string: str) -> str:
    return COLOR_RED + string + COLOR_RESET

def set_color_yellow(string: str) -> str:
    return COLOR_YELLOW + string + COLOR_RESET

def set_color_blue(string: str) -> str:
    return COLOR_BLUE + string + COLOR_RESET

def set_color_green(string: str) -> str:
    return COLOR_GREEN + string + COLOR_RESET

def set_color_magenta(string: str) -> str:
    return COLOR_MAGENTA + string + COLOR_RESET

def set_color_cyan(string: str) -> str:
    return COLOR_CYAN + string + COLOR_RESET

def set_color_white(string: str) -> str:
    return COLOR_WHITE + string + COLOR_RESET

def set_color_black(string: str) -> str:
    return COLOR_BLACK + string + COLOR_RESET

def set_color(string: str, color: str) -> str:
    return color + string + COLOR_RESET
