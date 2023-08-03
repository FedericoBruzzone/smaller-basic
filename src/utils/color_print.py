from src.utils import color

def ColorPrint(color_name: str) -> type: 
    """
    Decorator to apply color to print function of a class.
    
    Args: 
        color_name (str): name of the color to apply to print function.
    Returns:
        type: metaclass to apply color to print function.
    """
    class ColorPrintMeta(type):
        """
        Metaclass to apply color to print function of a class.
        """
        def __new__(cls: type, classname: str, supers: tuple, classdict: dict) -> type:
            for attr_name, attr_value in classdict.items():
                if callable(attr_value) and attr_name == "print":
                    classdict[attr_name] =  cls.decorate_print(attr_value, color_name)
                    classdict[attr_name].__qualname__ = attr_value.__qualname__
                    classdict[attr_name] = staticmethod(classdict[attr_name])
            return super().__new__(cls, classname, supers, classdict)
        
        def decorate_print(print_func: staticmethod, color_name: str) -> callable:
            """
            Decorator to apply color to a print function.

            Args:
                print_func (staticmethod): print function to apply color.
                color_name (str): name of the color to apply to print function.
            Returns:
                callable: decorated print function. 
            """
            def wrapper(*args, **kwargs):
                """
                Decorated print function.

                Args:
                    *args: arguments of the print function.
                    **kwargs: keyword arguments of the print function.
                """
                color_fuction = f"set_color_{color_name}"
                print_func(color.__dict__[color_fuction](args[0]))
                # print(color.__dict__[color_fuction](args[0]))
            return wrapper
    return ColorPrintMeta

def apply_color_print(cls: type, color_name: str) -> type:
    """
    Function to apply color to print function of a class.

    Args:
        cls (type): class to apply color to print function.
        color_name (str): name of the color to apply to print function.
    Returns:
        type: class with color applied to print function.
    """
    return ColorPrint(color_name)(cls.__name__, cls.__bases__, dict(cls.__dict__))

