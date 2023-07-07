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


    # Visit a parse tree produced by SmallerBasicParser#declarationStatement.
    def visitDeclarationStatement(self, ctx:SmallerBasicParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#whileStatement.
    def visitWhileStatement(self, ctx:SmallerBasicParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#ifStatement.
    def visitIfStatement(self, ctx:SmallerBasicParser.IfStatementContext):
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


    # Visit a parse tree produced by SmallerBasicParser#atomString.
    def visitAtomString(self, ctx:SmallerBasicParser.AtomStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#literal.
    def visitLiteral(self, ctx:SmallerBasicParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#signedNumber.
    def visitSignedNumber(self, ctx:SmallerBasicParser.SignedNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#string.
    def visitString(self, ctx:SmallerBasicParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#boolean.
    def visitBoolean(self, ctx:SmallerBasicParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#id.
    def visitId(self, ctx:SmallerBasicParser.IdContext):
        return self.visitChildren(ctx)



del SmallerBasicParser