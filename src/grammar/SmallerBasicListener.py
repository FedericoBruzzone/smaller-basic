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


    # Enter a parse tree produced by SmallerBasicParser#IfStatementWithElse.
    def enterIfStatementWithElse(self, ctx:SmallerBasicParser.IfStatementWithElseContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#IfStatementWithElse.
    def exitIfStatementWithElse(self, ctx:SmallerBasicParser.IfStatementWithElseContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#IfStatementWithoutElse.
    def enterIfStatementWithoutElse(self, ctx:SmallerBasicParser.IfStatementWithoutElseContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#IfStatementWithoutElse.
    def exitIfStatementWithoutElse(self, ctx:SmallerBasicParser.IfStatementWithoutElseContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#WhileStatementStandard.
    def enterWhileStatementStandard(self, ctx:SmallerBasicParser.WhileStatementStandardContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#WhileStatementStandard.
    def exitWhileStatementStandard(self, ctx:SmallerBasicParser.WhileStatementStandardContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#ForStatementStandard.
    def enterForStatementStandard(self, ctx:SmallerBasicParser.ForStatementStandardContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#ForStatementStandard.
    def exitForStatementStandard(self, ctx:SmallerBasicParser.ForStatementStandardContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#ForStatementWithStep.
    def enterForStatementWithStep(self, ctx:SmallerBasicParser.ForStatementWithStepContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#ForStatementWithStep.
    def exitForStatementWithStep(self, ctx:SmallerBasicParser.ForStatementWithStepContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#SubroutineStatementStandard.
    def enterSubroutineStatementStandard(self, ctx:SmallerBasicParser.SubroutineStatementStandardContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#SubroutineStatementStandard.
    def exitSubroutineStatementStandard(self, ctx:SmallerBasicParser.SubroutineStatementStandardContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#CallSubroutineStatementStandard.
    def enterCallSubroutineStatementStandard(self, ctx:SmallerBasicParser.CallSubroutineStatementStandardContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#CallSubroutineStatementStandard.
    def exitCallSubroutineStatementStandard(self, ctx:SmallerBasicParser.CallSubroutineStatementStandardContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#LibraryStatementWithParameters.
    def enterLibraryStatementWithParameters(self, ctx:SmallerBasicParser.LibraryStatementWithParametersContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#LibraryStatementWithParameters.
    def exitLibraryStatementWithParameters(self, ctx:SmallerBasicParser.LibraryStatementWithParametersContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#LibraryStatementWithoutParameters.
    def enterLibraryStatementWithoutParameters(self, ctx:SmallerBasicParser.LibraryStatementWithoutParametersContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#LibraryStatementWithoutParameters.
    def exitLibraryStatementWithoutParameters(self, ctx:SmallerBasicParser.LibraryStatementWithoutParametersContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#ArrayAccessStandard.
    def enterArrayAccessStandard(self, ctx:SmallerBasicParser.ArrayAccessStandardContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#ArrayAccessStandard.
    def exitArrayAccessStandard(self, ctx:SmallerBasicParser.ArrayAccessStandardContext):
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


    # Enter a parse tree produced by SmallerBasicParser#BooleanArithmeticalExpression.
    def enterBooleanArithmeticalExpression(self, ctx:SmallerBasicParser.BooleanArithmeticalExpressionContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#BooleanArithmeticalExpression.
    def exitBooleanArithmeticalExpression(self, ctx:SmallerBasicParser.BooleanArithmeticalExpressionContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#BooleanStringExpression.
    def enterBooleanStringExpression(self, ctx:SmallerBasicParser.BooleanStringExpressionContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#BooleanStringExpression.
    def exitBooleanStringExpression(self, ctx:SmallerBasicParser.BooleanStringExpressionContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#BooleanAtomExpression.
    def enterBooleanAtomExpression(self, ctx:SmallerBasicParser.BooleanAtomExpressionContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#BooleanAtomExpression.
    def exitBooleanAtomExpression(self, ctx:SmallerBasicParser.BooleanAtomExpressionContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomBooleanBoolean.
    def enterAtomBooleanBoolean(self, ctx:SmallerBasicParser.AtomBooleanBooleanContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomBooleanBoolean.
    def exitAtomBooleanBoolean(self, ctx:SmallerBasicParser.AtomBooleanBooleanContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomBooleanId.
    def enterAtomBooleanId(self, ctx:SmallerBasicParser.AtomBooleanIdContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomBooleanId.
    def exitAtomBooleanId(self, ctx:SmallerBasicParser.AtomBooleanIdContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomBooleanParenthesis.
    def enterAtomBooleanParenthesis(self, ctx:SmallerBasicParser.AtomBooleanParenthesisContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomBooleanParenthesis.
    def exitAtomBooleanParenthesis(self, ctx:SmallerBasicParser.AtomBooleanParenthesisContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomBooleanLibraryStatement.
    def enterAtomBooleanLibraryStatement(self, ctx:SmallerBasicParser.AtomBooleanLibraryStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomBooleanLibraryStatement.
    def exitAtomBooleanLibraryStatement(self, ctx:SmallerBasicParser.AtomBooleanLibraryStatementContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomBooleanArrayAccess.
    def enterAtomBooleanArrayAccess(self, ctx:SmallerBasicParser.AtomBooleanArrayAccessContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomBooleanArrayAccess.
    def exitAtomBooleanArrayAccess(self, ctx:SmallerBasicParser.AtomBooleanArrayAccessContext):
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


    # Enter a parse tree produced by SmallerBasicParser#unaryAtomNumber.
    def enterUnaryAtomNumber(self, ctx:SmallerBasicParser.UnaryAtomNumberContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#unaryAtomNumber.
    def exitUnaryAtomNumber(self, ctx:SmallerBasicParser.UnaryAtomNumberContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomNumberInt.
    def enterAtomNumberInt(self, ctx:SmallerBasicParser.AtomNumberIntContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomNumberInt.
    def exitAtomNumberInt(self, ctx:SmallerBasicParser.AtomNumberIntContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomNumberFloat.
    def enterAtomNumberFloat(self, ctx:SmallerBasicParser.AtomNumberFloatContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomNumberFloat.
    def exitAtomNumberFloat(self, ctx:SmallerBasicParser.AtomNumberFloatContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomNumberId.
    def enterAtomNumberId(self, ctx:SmallerBasicParser.AtomNumberIdContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomNumberId.
    def exitAtomNumberId(self, ctx:SmallerBasicParser.AtomNumberIdContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomNumberParenthesis.
    def enterAtomNumberParenthesis(self, ctx:SmallerBasicParser.AtomNumberParenthesisContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomNumberParenthesis.
    def exitAtomNumberParenthesis(self, ctx:SmallerBasicParser.AtomNumberParenthesisContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomNumberLibraryStatement.
    def enterAtomNumberLibraryStatement(self, ctx:SmallerBasicParser.AtomNumberLibraryStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomNumberLibraryStatement.
    def exitAtomNumberLibraryStatement(self, ctx:SmallerBasicParser.AtomNumberLibraryStatementContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomNumberArrayAccess.
    def enterAtomNumberArrayAccess(self, ctx:SmallerBasicParser.AtomNumberArrayAccessContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomNumberArrayAccess.
    def exitAtomNumberArrayAccess(self, ctx:SmallerBasicParser.AtomNumberArrayAccessContext):
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


    # Enter a parse tree produced by SmallerBasicParser#AtomStringParenthesis.
    def enterAtomStringParenthesis(self, ctx:SmallerBasicParser.AtomStringParenthesisContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomStringParenthesis.
    def exitAtomStringParenthesis(self, ctx:SmallerBasicParser.AtomStringParenthesisContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomStringLibraryStatement.
    def enterAtomStringLibraryStatement(self, ctx:SmallerBasicParser.AtomStringLibraryStatementContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomStringLibraryStatement.
    def exitAtomStringLibraryStatement(self, ctx:SmallerBasicParser.AtomStringLibraryStatementContext):
        pass


    # Enter a parse tree produced by SmallerBasicParser#AtomStringArrayAccess.
    def enterAtomStringArrayAccess(self, ctx:SmallerBasicParser.AtomStringArrayAccessContext):
        pass

    # Exit a parse tree produced by SmallerBasicParser#AtomStringArrayAccess.
    def exitAtomStringArrayAccess(self, ctx:SmallerBasicParser.AtomStringArrayAccessContext):
        pass



del SmallerBasicParser