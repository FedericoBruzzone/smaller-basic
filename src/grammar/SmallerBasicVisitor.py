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


    # Visit a parse tree produced by SmallerBasicParser#IfStatementWithElse.
    def visitIfStatementWithElse(self, ctx:SmallerBasicParser.IfStatementWithElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#IfStatementWithoutElse.
    def visitIfStatementWithoutElse(self, ctx:SmallerBasicParser.IfStatementWithoutElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#WhileStatementStandard.
    def visitWhileStatementStandard(self, ctx:SmallerBasicParser.WhileStatementStandardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#ForStatementStandard.
    def visitForStatementStandard(self, ctx:SmallerBasicParser.ForStatementStandardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#ForStatementWithStep.
    def visitForStatementWithStep(self, ctx:SmallerBasicParser.ForStatementWithStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#subroutineStatement.
    def visitSubroutineStatement(self, ctx:SmallerBasicParser.SubroutineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#callSubroutineStatement.
    def visitCallSubroutineStatement(self, ctx:SmallerBasicParser.CallSubroutineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#LibraryStatementWithParameters.
    def visitLibraryStatementWithParameters(self, ctx:SmallerBasicParser.LibraryStatementWithParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#LibraryStatementWithoutParameters.
    def visitLibraryStatementWithoutParameters(self, ctx:SmallerBasicParser.LibraryStatementWithoutParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#expression.
    def visitExpression(self, ctx:SmallerBasicParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#logicalExpression.
    def visitLogicalExpression(self, ctx:SmallerBasicParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#BooleanArithmeticalExpression.
    def visitBooleanArithmeticalExpression(self, ctx:SmallerBasicParser.BooleanArithmeticalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#BooleanStringExpression.
    def visitBooleanStringExpression(self, ctx:SmallerBasicParser.BooleanStringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#BooleanAtomExpression.
    def visitBooleanAtomExpression(self, ctx:SmallerBasicParser.BooleanAtomExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#AtomBooleanBoolean.
    def visitAtomBooleanBoolean(self, ctx:SmallerBasicParser.AtomBooleanBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#AtomBooleanId.
    def visitAtomBooleanId(self, ctx:SmallerBasicParser.AtomBooleanIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#AtomBooleanParenthesis.
    def visitAtomBooleanParenthesis(self, ctx:SmallerBasicParser.AtomBooleanParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#AtomBooleanLibraryStatement.
    def visitAtomBooleanLibraryStatement(self, ctx:SmallerBasicParser.AtomBooleanLibraryStatementContext):
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


    # Visit a parse tree produced by SmallerBasicParser#unaryAtomNumber.
    def visitUnaryAtomNumber(self, ctx:SmallerBasicParser.UnaryAtomNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#AtomNumberInt.
    def visitAtomNumberInt(self, ctx:SmallerBasicParser.AtomNumberIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#AtomNumberFloat.
    def visitAtomNumberFloat(self, ctx:SmallerBasicParser.AtomNumberFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#AtomNumberId.
    def visitAtomNumberId(self, ctx:SmallerBasicParser.AtomNumberIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#AtomNumberParenthesis.
    def visitAtomNumberParenthesis(self, ctx:SmallerBasicParser.AtomNumberParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#AtomNumberLibraryStatement.
    def visitAtomNumberLibraryStatement(self, ctx:SmallerBasicParser.AtomNumberLibraryStatementContext):
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


    # Visit a parse tree produced by SmallerBasicParser#AtomStringParenthesis.
    def visitAtomStringParenthesis(self, ctx:SmallerBasicParser.AtomStringParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmallerBasicParser#AtomStringLibraryStatement.
    def visitAtomStringLibraryStatement(self, ctx:SmallerBasicParser.AtomStringLibraryStatementContext):
        return self.visitChildren(ctx)



del SmallerBasicParser