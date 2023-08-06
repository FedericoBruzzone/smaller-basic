# Generated from src/grammar/SmallerBasic.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SmallerBasicParser import SmallerBasicParser
else:
    from SmallerBasicParser import SmallerBasicParser

# This class defines a complete generic visitor for a parse tree produced by SmallerBasicParser.

class SmallerBasicVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SmallerBasicParser#program.
    def visitProgram(self, ctx:SmallerBasicParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#statement.
    def visitStatement(self, ctx:SmallerBasicParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#VariableDeclarationStatement.
    def visitVariableDeclarationStatement(self, ctx:SmallerBasicParser.VariableDeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#ArrayDeclarationStatement.
    def visitArrayDeclarationStatement(self, ctx:SmallerBasicParser.ArrayDeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#labelStatement.
    def visitLabelStatement(self, ctx:SmallerBasicParser.LabelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#gotoStatement.
    def visitGotoStatement(self, ctx:SmallerBasicParser.GotoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#ifStatement.
    def visitIfStatement(self, ctx:SmallerBasicParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#whileStatement.
    def visitWhileStatement(self, ctx:SmallerBasicParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#forStatement.
    def visitForStatement(self, ctx:SmallerBasicParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#subroutineStatement.
    def visitSubroutineStatement(self, ctx:SmallerBasicParser.SubroutineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#callSubroutineStatement.
    def visitCallSubroutineStatement(self, ctx:SmallerBasicParser.CallSubroutineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#libraryStatement.
    def visitLibraryStatement(self, ctx:SmallerBasicParser.LibraryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#expression.
    def visitExpression(self, ctx:SmallerBasicParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#logicalExpression.
    def visitLogicalExpression(self, ctx:SmallerBasicParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#booleanExpression.
    def visitBooleanExpression(self, ctx:SmallerBasicParser.BooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#atomBoolean.
    def visitAtomBoolean(self, ctx:SmallerBasicParser.AtomBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#arithmeticalExpression.
    def visitArithmeticalExpression(self, ctx:SmallerBasicParser.ArithmeticalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:SmallerBasicParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:SmallerBasicParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#atomNumber.
    def visitAtomNumber(self, ctx:SmallerBasicParser.AtomNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#stringExpression.
    def visitStringExpression(self, ctx:SmallerBasicParser.StringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#additiveStringExpression.
    def visitAdditiveStringExpression(self, ctx:SmallerBasicParser.AdditiveStringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#AtomStringLiteral.
    def visitAtomStringLiteral(self, ctx:SmallerBasicParser.AtomStringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#AtomStringId.
    def visitAtomStringId(self, ctx:SmallerBasicParser.AtomStringIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#AtomStringLibraryStatement.
    def visitAtomStringLibraryStatement(self, ctx:SmallerBasicParser.AtomStringLibraryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#literal.
    def visitLiteral(self, ctx:SmallerBasicParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#signedInt.
    def visitSignedInt(self, ctx:SmallerBasicParser.SignedIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#signedFloat.
    def visitSignedFloat(self, ctx:SmallerBasicParser.SignedFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#string.
    def visitString(self, ctx:SmallerBasicParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#boolean.
    def visitBoolean(self, ctx:SmallerBasicParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#signedId.
    def visitSignedId(self, ctx:SmallerBasicParser.SignedIdContext):
        return self.visitChildren(ctx)



del SmallerBasicParser