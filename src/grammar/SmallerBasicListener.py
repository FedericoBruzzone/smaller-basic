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


    # Enter a parse tree produced by SmallerBasicParser#declarationStatement.
    def enterDeclarationStatement(self, ctx:SmallerBasicParser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#declarationStatement.
    def exitDeclarationStatement(self, ctx:SmallerBasicParser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#expression.
    def enterExpression(self, ctx:SmallerBasicParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#expression.
    def exitExpression(self, ctx:SmallerBasicParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#logicalExpression.
    def enterLogicalExpression(self, ctx:SmallerBasicParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#logicalExpression.
    def exitLogicalExpression(self, ctx:SmallerBasicParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#booleanExpression.
    def enterBooleanExpression(self, ctx:SmallerBasicParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#booleanExpression.
    def exitBooleanExpression(self, ctx:SmallerBasicParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#atomBoolean.
    def enterAtomBoolean(self, ctx:SmallerBasicParser.AtomBooleanContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#atomBoolean.
    def exitAtomBoolean(self, ctx:SmallerBasicParser.AtomBooleanContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#arithmeticalExpression.
    def enterArithmeticalExpression(self, ctx:SmallerBasicParser.ArithmeticalExpressionContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#arithmeticalExpression.
    def exitArithmeticalExpression(self, ctx:SmallerBasicParser.ArithmeticalExpressionContext):
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


    # Enter a parse tree produced by SmallerBasicParser#atomNumber.
    def enterAtomNumber(self, ctx:SmallerBasicParser.AtomNumberContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#atomNumber.
    def exitAtomNumber(self, ctx:SmallerBasicParser.AtomNumberContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#stringExpression.
    def enterStringExpression(self, ctx:SmallerBasicParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#stringExpression.
    def exitStringExpression(self, ctx:SmallerBasicParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#additiveStringExpression.
    def enterAdditiveStringExpression(self, ctx:SmallerBasicParser.AdditiveStringExpressionContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#additiveStringExpression.
    def exitAdditiveStringExpression(self, ctx:SmallerBasicParser.AdditiveStringExpressionContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#atomString.
    def enterAtomString(self, ctx:SmallerBasicParser.AtomStringContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#atomString.
    def exitAtomString(self, ctx:SmallerBasicParser.AtomStringContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#literal.
    def enterLiteral(self, ctx:SmallerBasicParser.LiteralContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#literal.
    def exitLiteral(self, ctx:SmallerBasicParser.LiteralContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#signedNumber.
    def enterSignedNumber(self, ctx:SmallerBasicParser.SignedNumberContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#signedNumber.
    def exitSignedNumber(self, ctx:SmallerBasicParser.SignedNumberContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#string.
    def enterString(self, ctx:SmallerBasicParser.StringContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#string.
    def exitString(self, ctx:SmallerBasicParser.StringContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#boolean.
    def enterBoolean(self, ctx:SmallerBasicParser.BooleanContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#boolean.
    def exitBoolean(self, ctx:SmallerBasicParser.BooleanContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#id.
    def enterId(self, ctx:SmallerBasicParser.IdContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#id.
    def exitId(self, ctx:SmallerBasicParser.IdContext):
        pass



del SmallerBasicParser