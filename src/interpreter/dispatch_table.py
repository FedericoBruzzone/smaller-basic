from typing import Any
import operator

class DispatchTable(object):
    """
    Dispatch table for the interpreter.
    """

    def __init__(self):
        self.dispatch_table_binary: dict = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : operator.truediv,
            "=" : operator.eq,
            "<>" : operator.ne,
            ">=" : operator.ge,
            "<=" : operator.le,
            ">" : operator.gt,
            "<" : operator.lt,
            "And" : operator.and_,
            "Or" : operator.or_,
        }
        self.dispatch_table_unary: dict = {
            "+" : operator.pos,
            "-" : operator.neg
        }
    
    def apply_binary(self, operator: str, left: Any, right: Any) -> Any:
        return self.dispatch_table_binary[operator](left, right)

    def apply_unary(self, operator: str, operand: Any) -> Any:
        return self.dispatch_table_unary[operator](operand)

    def get_dispatch_table(self) -> dict:
        return self.dispatch_table

