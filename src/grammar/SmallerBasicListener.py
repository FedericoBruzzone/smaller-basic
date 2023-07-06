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


    # Enter a parse tree produced by SmallerBasicParser#additiveStringExpression.
    def enterAdditiveStringExpression(self, ctx:SmallerBasicParser.AdditiveStringExpressionContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#additiveStringExpression.
    def exitAdditiveStringExpression(self, ctx:SmallerBasicParser.AdditiveStringExpressionContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:SmallerBasicParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:SmallerBasicParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:SmallerBasicParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:SmallerBasicParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#atomString.
    def enterAtomString(self, ctx:SmallerBasicParser.AtomStringContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#atomString.
    def exitAtomString(self, ctx:SmallerBasicParser.AtomStringContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#atom.
    def enterAtom(self, ctx:SmallerBasicParser.AtomContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#atom.
    def exitAtom(self, ctx:SmallerBasicParser.AtomContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#literal.
    def enterLiteral(self, ctx:SmallerBasicParser.LiteralContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#literal.
    def exitLiteral(self, ctx:SmallerBasicParser.LiteralContext):
        pass



del SmallerBasicParser