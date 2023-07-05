# Generated from src/grammar/SmallerBasic.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SmallerBasicParser import SmallerBasicParser
else:
    from SmallerBasicParser import SmallerBasicParser

# This class defines a complete listener for a parse tree produced by SmallerBasicParser.
class SmallerBasicListener(ParseTreeListener):

    # Enter a parse tree produced by SmallerBasicParser#program.
    def enterProgram(self, ctx:SmallerBasicParser.ProgramContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#program.
    def exitProgram(self, ctx:SmallerBasicParser.ProgramContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#statement.
    def enterStatement(self, ctx:SmallerBasicParser.StatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#statement.
    def exitStatement(self, ctx:SmallerBasicParser.StatementContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#expression.
    def enterExpression(self, ctx:SmallerBasicParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#expression.
    def exitExpression(self, ctx:SmallerBasicParser.ExpressionContext):
        pass



del SmallerBasicParser