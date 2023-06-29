from src.utils import color

def ColorPrint(color_name: str) -> type: 
    class ColorPrintMeta(type):
        def __new__(cls, classname, supers, classdict) -> type:
            for attr_name, attr_value in classdict.items():
                if callable(attr_value) and attr_name == "print":
                    classdict[attr_name] =  cls.decorate_print(attr_value, color_name)
                    classdict[attr_name].__qualname__ = attr_value.__qualname__
                    classdict[attr_name] = staticmethod(classdict[attr_name])
            return super().__new__(cls, classname, supers, classdict)
        
        def decorate_print(print_func: staticmethod, color_name: str) -> callable:
            def wrapper(*args, **kwargs):
                color_fuction = f"set_color_{color_name}"
                print_func(color.__dict__[color_fuction](args[0]))
                # print(color.__dict__[color_fuction](args[0]))
            return wrapper
    return ColorPrintMeta

def apply_color_print(cls: type, color_name: str):
    return ColorPrint(color_name)(cls.__name__, (object, ), dict(cls.__dict__))
