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


    # Enter a parse tree produced by SmallerBasicParser#VariableDeclarationStatement.
    def enterVariableDeclarationStatement(self, ctx:SmallerBasicParser.VariableDeclarationStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#VariableDeclarationStatement.
    def exitVariableDeclarationStatement(self, ctx:SmallerBasicParser.VariableDeclarationStatementContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#ArrayDeclarationStatement.
    def enterArrayDeclarationStatement(self, ctx:SmallerBasicParser.ArrayDeclarationStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#ArrayDeclarationStatement.
    def exitArrayDeclarationStatement(self, ctx:SmallerBasicParser.ArrayDeclarationStatementContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#labelStatement.
    def enterLabelStatement(self, ctx:SmallerBasicParser.LabelStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#labelStatement.
    def exitLabelStatement(self, ctx:SmallerBasicParser.LabelStatementContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#gotoStatement.
    def enterGotoStatement(self, ctx:SmallerBasicParser.GotoStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#gotoStatement.
    def exitGotoStatement(self, ctx:SmallerBasicParser.GotoStatementContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#ifStatement.
    def enterIfStatement(self, ctx:SmallerBasicParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#ifStatement.
    def exitIfStatement(self, ctx:SmallerBasicParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#whileStatement.
    def enterWhileStatement(self, ctx:SmallerBasicParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#whileStatement.
    def exitWhileStatement(self, ctx:SmallerBasicParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#forStatement.
    def enterForStatement(self, ctx:SmallerBasicParser.ForStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#forStatement.
    def exitForStatement(self, ctx:SmallerBasicParser.ForStatementContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#subroutineStatement.
    def enterSubroutineStatement(self, ctx:SmallerBasicParser.SubroutineStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#subroutineStatement.
    def exitSubroutineStatement(self, ctx:SmallerBasicParser.SubroutineStatementContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#callSubroutineStatement.
    def enterCallSubroutineStatement(self, ctx:SmallerBasicParser.CallSubroutineStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#callSubroutineStatement.
    def exitCallSubroutineStatement(self, ctx:SmallerBasicParser.CallSubroutineStatementContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#libraryStatement.
    def enterLibraryStatement(self, ctx:SmallerBasicParser.LibraryStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#libraryStatement.
    def exitLibraryStatement(self, ctx:SmallerBasicParser.LibraryStatementContext):
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


    # Enter a parse tree produced by SmallerBasicParser#AtomIntLiteral.
    def enterAtomIntLiteral(self, ctx:SmallerBasicParser.AtomIntLiteralContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomIntLiteral.
    def exitAtomIntLiteral(self, ctx:SmallerBasicParser.AtomIntLiteralContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomFloatLiteral.
    def enterAtomFloatLiteral(self, ctx:SmallerBasicParser.AtomFloatLiteralContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomFloatLiteral.
    def exitAtomFloatLiteral(self, ctx:SmallerBasicParser.AtomFloatLiteralContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomNumberId.
    def enterAtomNumberId(self, ctx:SmallerBasicParser.AtomNumberIdContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomNumberId.
    def exitAtomNumberId(self, ctx:SmallerBasicParser.AtomNumberIdContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomNumberArithmeticalExpression.
    def enterAtomNumberArithmeticalExpression(self, ctx:SmallerBasicParser.AtomNumberArithmeticalExpressionContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomNumberArithmeticalExpression.
    def exitAtomNumberArithmeticalExpression(self, ctx:SmallerBasicParser.AtomNumberArithmeticalExpressionContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomNumberLibraryStatement.
    def enterAtomNumberLibraryStatement(self, ctx:SmallerBasicParser.AtomNumberLibraryStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomNumberLibraryStatement.
    def exitAtomNumberLibraryStatement(self, ctx:SmallerBasicParser.AtomNumberLibraryStatementContext):
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


    # Enter a parse tree produced by SmallerBasicParser#AtomStringLiteral.
    def enterAtomStringLiteral(self, ctx:SmallerBasicParser.AtomStringLiteralContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomStringLiteral.
    def exitAtomStringLiteral(self, ctx:SmallerBasicParser.AtomStringLiteralContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomStringId.
    def enterAtomStringId(self, ctx:SmallerBasicParser.AtomStringIdContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomStringId.
    def exitAtomStringId(self, ctx:SmallerBasicParser.AtomStringIdContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomStringLibraryStatement.
    def enterAtomStringLibraryStatement(self, ctx:SmallerBasicParser.AtomStringLibraryStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomStringLibraryStatement.
    def exitAtomStringLibraryStatement(self, ctx:SmallerBasicParser.AtomStringLibraryStatementContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#literal.
    def enterLiteral(self, ctx:SmallerBasicParser.LiteralContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#literal.
    def exitLiteral(self, ctx:SmallerBasicParser.LiteralContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#signedInt.
    def enterSignedInt(self, ctx:SmallerBasicParser.SignedIntContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#signedInt.
    def exitSignedInt(self, ctx:SmallerBasicParser.SignedIntContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#signedFloat.
    def enterSignedFloat(self, ctx:SmallerBasicParser.SignedFloatContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#signedFloat.
    def exitSignedFloat(self, ctx:SmallerBasicParser.SignedFloatContext):
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


    # Enter a parse tree produced by SmallerBasicParser#signedId.
    def enterSignedId(self, ctx:SmallerBasicParser.SignedIdContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#signedId.
    def exitSignedId(self, ctx:SmallerBasicParser.SignedIdContext):
        pass



del SmallerBasicParser