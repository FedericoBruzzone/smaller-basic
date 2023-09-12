from antlr4 import ParserRuleContext

from typing import List
from src.grammar.SmallerBasicVisitor import SmallerBasicVisitor
from src.grammar.SmallerBasicParser import SmallerBasicParser

from src.abstract_syntax_tree.ast import Ast
from src.abstract_syntax_tree.statement_nodes.abstract_statement_node import AbstractStatementNode
# ======================================================
# ===================== STATEMENTS =====================
# ======================================================
from src.abstract_syntax_tree.statement_nodes.abstract_statement_node import AbstractStatementNode
from src.abstract_syntax_tree.statement_nodes.statements_node import StatementsNode
# ==================== DECLARATION STATEMENTS ====================
from src.abstract_syntax_tree.statement_nodes.declaration_statement_nodes.varible_declaration_statement_node import VariableDeclarationStatementNode
from src.abstract_syntax_tree.statement_nodes.declaration_statement_nodes.array_declaration_statement_node import ArrayDeclarationStatementNode
# ==================== LIBRARY STATEMENTS ====================
from src.abstract_syntax_tree.statement_nodes.library_statement_nodes.library_statement_node_with_parameters import LibraryStatementWithParametersNode

from src.abstract_syntax_tree.statement_nodes.library_statement_nodes.library_statement_node_without_parameters import LibraryStatementWithoutParametersNode
# ==================== IF STATEMENTS ====================
from src.abstract_syntax_tree.statement_nodes.if_statement_nodes.if_statement_with_else_node import IfStatementWithElseNode
from src.abstract_syntax_tree.statement_nodes.if_statement_nodes.if_statement_without_else_node import IfStatementWithoutElseNode
# ==================== WHILE STATEMENTS ====================
from src.abstract_syntax_tree.statement_nodes.while_statement_nodes.while_statement_standard_node import WhileStatementStandardNode
# ==================== FOR STATEMENTS ====================
from src.abstract_syntax_tree.statement_nodes.for_statement_nodes.for_statement_standard_node import ForStatementStandardNode
from src.abstract_syntax_tree.statement_nodes.for_statement_nodes.for_statement_with_step_node import ForStatementWithStepNode
# ==================== SUBROUTINE STATEMENTS ====================
from src.abstract_syntax_tree.statement_nodes.subroutine_statement_nodes.subroutine_statement_standard_node import SubroutineStatementStandardNode
from src.abstract_syntax_tree.statement_nodes.subroutine_statement_nodes.call_subroutine_statement_standard_node import CallSubroutineStatementStandardNode
# ==================== GOTO and LABEL STATEMENTS ====================
from src.abstract_syntax_tree.statement_nodes.goto_label_statement_nodes.goto_statement_standard_node import GotoStatementStandardNode
from src.abstract_syntax_tree.statement_nodes.goto_label_statement_nodes.label_statement_standard_node import LabelStatementStandardNode

# ======================================================
# ===================== EXPRESSIONS ====================
# ======================================================
from src.abstract_syntax_tree.expression_nodes.abstract_expression_node import AbstractExpressionNode
from src.abstract_syntax_tree.expression_nodes.expressions_node import ExpressionsNode
# ==================== LOGICAL AND BOOELAN EXPRESSIONS ====================
from src.abstract_syntax_tree.expression_nodes.logical_boolean_expression_nodes.logical_expression_node import LogicalExpressionNode
from src.abstract_syntax_tree.expression_nodes.logical_boolean_expression_nodes.boolean_arithmetical_expression_node import BooleanArithmeticalExpressionNode
from src.abstract_syntax_tree.expression_nodes.logical_boolean_expression_nodes.boolean_string_expression_node import BooleanStringExpressionNode
# ==================== ARITHMETICAL EXPRESSIONS ====================
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.additive_expression_node import AdditiveExpressionNode
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.multiplicative_expression_node import MultiplicativeExpressionNode
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.unary_atom_number_node import UnaryAtomNumberNode
# ==================== STRING EXPRESSIONS ====================
from src.abstract_syntax_tree.expression_nodes.string_expression_nodes.additive_string_expression_node import AdditiveStringExpressionNode

# ======================================================
# ======================= TOKENS =======================
# ======================================================
from src.abstract_syntax_tree.token_nodes.id_node import IdNode
from src.abstract_syntax_tree.token_nodes.string_node import StringNode
from src.abstract_syntax_tree.token_nodes.int_node import IntNode
from src.abstract_syntax_tree.token_nodes.float_node import FloatNode
from src.abstract_syntax_tree.token_nodes.boolean_node import BooleanNode
# ==================== ARRAY ACCESS ====================
from src.abstract_syntax_tree.token_nodes.id_array_node import IdArrayNode

def get_unary_sign(ctx: ParserRuleContext) -> str:
    """
    Get unary sign of the given context.

    Returns:
        str: unary sign of the given context.
    """
    if ctx.PLUS():
        return '+'
    elif ctx.MINUS():
        return '-'
    else:
        return ""

class SmallerBasicAstVisitor(SmallerBasicVisitor):
    """
    This class visits the parse tree and creates an abstract syntax tree.
    """
    def visitProgram(self, ctx: SmallerBasicParser.ProgramContext) -> Ast:
        """
        Visit Program node in parse tree

        Parameters:
            ctx (SmallerBasicParser.ProgramContext): The parse tree
        """
        statements: List[AbstractStatementNode] = [
            self.visit(child) for child in ctx.statement()]
        return Ast(statements)

    # ======================================================
    # ===================== STATEMENTS =====================
    # ======================================================

    def visitStatement(self, ctx: SmallerBasicParser.StatementContext):
        """
        Visit Statement node in parse tree

        Parameters:
            ctx (SmallerBasicParser.StatementContext): The parse tree
        """
        return super().visitStatement(ctx)

    # ==================== DECLARATION STATEMENTS ====================

    def visitVariableDeclarationStatement(self, ctx: SmallerBasicParser.VariableDeclarationStatementContext):
        """
        Visit VariableDeclarationStatement node in parse tree

        Parameters:
            ctx (SmallerBasicParser.VariableDeclarationStatementContext): The parse tree
        """
        return VariableDeclarationStatementNode(
            IdNode(ctx.ID().getText()),
            self.visit(ctx.expression())
        )

    def visitArrayDeclarationStatement(self, ctx: SmallerBasicParser.ArrayDeclarationStatementContext):
        """
        Visit ArrayDeclarationStatement node in parse tree

        Parameters:
            ctx (SmallerBasicParser.ArrayDeclarationStatementContext): The parse tree
        """
        # ID (LSQUARE arithmeticalExpression RSQUARE)+ EQ expression
        #    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        _, *arithmetical_expressions, _, _ = ctx.children
        arithmetical_expressions: list = [i for i in arithmetical_expressions if i.getText() not in [ctx.LSQUARE()[0].getText(), ctx.RSQUARE()[0].getText()]]

        return ArrayDeclarationStatementNode(
            IdNode(ctx.ID().getText()),
            ExpressionsNode([self.visit(i) for i in arithmetical_expressions]),
            self.visit(ctx.expression())
        )

    # ==================== LIBRARY STATEMENTS ====================
    def visitLibraryStatementWithParameters(self, ctx: SmallerBasicParser.LibraryStatementWithParametersContext):
        """
        Visit LibraryStatementWithParameters node in parse tree

        Parameters:
            ctx (SmallerBasicParser.LibraryStatementWithoutParametersContext): The parse tree
        """
        lib_name: str = IdNode(ctx.ID(0).getText())
        func_name: str = IdNode(ctx.ID(1).getText())
        exp0 = self.visit(ctx.expression(0))
        # ID DOT ID LROUND expression (COMMA expression)+ RROUND
        #                             ^^^^^^^^^^^^^^^^^^^
        _, _, _, _, _, *expressions, _ = ctx.children
        exp1toN: list = [i for i in expressions if i.getText() not in [ctx.COMMA()[0].getText()]]
        return LibraryStatementWithParametersNode(
            lib_name,
            func_name,
            ExpressionsNode([exp0] + [self.visit(i) for i in exp1toN])
        )

    # def visitLibraryStatementWithParameter(self, ctx: SmallerBasicParser.LibraryStatementWithParameterContext):
    #     """
    #     Visit LibraryStatementWithParameter node in parse tree
    #
    #     Parameters:
    #         ctx (SmallerBasicParser.LibraryStatementWithParameterContext): The parse tree
    #     """
    #     return LibraryStatementWithParameterNode(
    #         IdNode(ctx.ID(0).getText()),
    #         IdNode(ctx.ID(1).getText()),
    #         self.visit(ctx.expression())
    #     )

    def visitLibraryStatementWithoutParameters(self, ctx: SmallerBasicParser.LibraryStatementWithoutParametersContext):
        """
        Visit LibraryStatementWithoutParameters node in parse tree

        Parameters:
            ctx (SmallerBasicParser.LibraryStatementWithoutParametersContext): The parse tree
        """
        return LibraryStatementWithoutParametersNode(
            IdNode(ctx.ID(0).getText()),
            IdNode(ctx.ID(1).getText())
        )

    # ==================== IF STATEMENTS ====================
    def visitIfStatementWithElse(self, ctx: SmallerBasicParser.IfStatementWithElseContext):
        """
        Visit IfStatementWithElse node in parse tree

        Parameters:
            ctx (SmallerBasicParser.IfStatementWithElseContext): The parse tree
        """
        # IF LROUND logicalExpression RROUND THEN statement+ ELSE statement+ ENDIF
        #                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^
        _, _, _, _, _, *statements, _ = ctx.children
        else_index: int = statements.index(ctx.ELSE())

        return IfStatementWithElseNode(
            self.visit(ctx.logicalExpression()),
            StatementsNode([self.visit(statement) for statement in statements[:else_index]]),
            StatementsNode([self.visit(statement) for statement in statements[else_index + 1:]])
        )

    def visitIfStatementWithoutElse(self, ctx: SmallerBasicParser.IfStatementWithoutElseContext):
        """
        Visit IfStatementWithoutElse node in parse tree

        Parameters:
            ctx (SmallerBasicParser.IfStatementWithoutElseContext): The parse tree
        """
        # IF LROUND logicalExpression RROUND THEN statement+ ENDIF
        #                                         ^^^^^^^^^^
        _, _, _, _, _, *statements, _ = ctx.children
        return IfStatementWithoutElseNode(
            self.visit(ctx.logicalExpression()),
            StatementsNode([self.visit(statement) for statement in statements])
        )

    # ==================== WHILE STATEMENTS ====================
    def visitWhileStatementStandard(self, ctx: SmallerBasicParser.WhileStatementStandardContext):
        """
        Visit WhileStatementStandard node in parse tree

        Parameters:
            ctx (SmallerBasicParser.WhileStatementStandardContext): The parse tree
        """
        # WHILE LROUND logicalExpression RROUND statement+ ENDWHILE
        #                                       ^^^^^^^^^^
        _, _, _, _, *statements, _ = ctx.children
        return WhileStatementStandardNode(
            self.visit(ctx.logicalExpression()),
            StatementsNode([self.visit(statement) for statement in statements])
        )

    # ==================== FOR STATEMENTS ====================
    def visitForStatementStandard(self, ctx: SmallerBasicParser.ForStatementStandardContext):
        """
        Visit ForStatementStandard node in parse tree

        Parameters:
            ctx (SmallerBasicParser.ForStatementStandardContext): The parse tree
        """
        # FOR ID EQ arithmeticalExpression TO arithmeticalExpression statement+ ENDFOR
        #                                                            ^^^^^^^^^^
        _, _, _, _, _, _, *statements, _ = ctx.children
        return ForStatementStandardNode(
            VariableDeclarationStatementNode(IdNode(ctx.ID().getText()),
                                             self.visit(ctx.arithmeticalExpression(0))),
            self.visit(ctx.arithmeticalExpression(1)),
            StatementsNode([self.visit(statement) for statement in statements])
        )

    def visitForStatementWithStep(self, ctx: SmallerBasicParser.ForStatementWithStepContext):
        """
        Visit ForStatementWithStep node in parse tree

        Parameters:
            ctx (SmallerBasicParser.ForStatementWithStepContext): The parse tree
        """
        # FOR ID EQ arithmeticalExpression TO arithmeticalExpression STEP arithmeticalExpression statement+ ENDFOR
        #                                                                                        ^^^^^^^^^^
        _, _, _, _, _, _, _, _, *statements, _ = ctx.children
        return ForStatementWithStepNode(
            VariableDeclarationStatementNode(IdNode(ctx.ID().getText()),
                                             self.visit(ctx.arithmeticalExpression(0))),
            self.visit(ctx.arithmeticalExpression(1)),
            self.visit(ctx.arithmeticalExpression(2)),
            StatementsNode([self.visit(statement) for statement in statements])
        )

    # ==================== SUBROUTINE STATEMENTS ====================
    def visitSubroutineStatementStandard(self, ctx: SmallerBasicParser.SubroutineStatementStandardContext):
        """
        Visit SubroutineStatementStandard node in parse tree

        Parameters:
            ctx (SmallerBasicParser.SubroutineStatementStandardContext): The parse tree
        """
        # SUBROUTINE ID statement+ ENDSUBROUTINE
        #               ^^^^^^^^^^
        _, _, *statements, _ = ctx.children
        return SubroutineStatementStandardNode(
            IdNode(ctx.ID().getText()),
            StatementsNode([self.visit(statement) for statement in statements])
        )

    def visitCallSubroutineStatementStandard(self, ctx: SmallerBasicParser.CallSubroutineStatementStandardContext):
        """
        Visit CallSubroutineStatementStandard node in parse tree

        Parameters:
            ctx (SmallerBasicParser.CallSubroutineStatementStandardContext): The parse tree
        """
        return CallSubroutineStatementStandardNode(IdNode(ctx.ID().getText()))

    # ==================== GOTO and LABEL STATEMENTS ====================
    def visitGotoStatement(self, ctx: SmallerBasicParser.GotoStatementContext):
        """
        Visit GotoStatement node in parse tree

        Parameters:
            ctx (SmallerBasicParser.GotoStatementContext): The parse tree
        """
        return GotoStatementStandardNode(IdNode(ctx.ID().getText()))

    def visitLabelStatement(self, ctx: SmallerBasicParser.LabelStatementContext):
        """
        Visit LabelStatement node in parse tree

        Parameters:
            ctx (SmallerBasicParser.LabelStatementContext): The parse tree
        """
        return LabelStatementStandardNode(IdNode(ctx.ID().getText()))

    # ==================== ARRAY ACCESS ====================
    def visitArrayAccessStandard(self, ctx: SmallerBasicParser.ArrayAccessStandardContext):
        """
        Visit ArrayAccessStandard node in parse tree

        Parameters:
            ctx (SmallerBasicParser.ArrayAccessStandardContext): The parse tree
        """
        # ID (LSQUARE arithmeticalExpression RSQUARE)+
        #    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        _, _, *arithmetical_expressions, _ = ctx.children
        arithmetical_expressions: list = [i for i in arithmetical_expressions if i.getText() not in [ctx.LSQUARE()[0].getText(), ctx.RSQUARE()[0].getText()]]

        return IdArrayNode(ctx.ID().getText(), ExpressionsNode([self.visit(i) for i in arithmetical_expressions]))


    # ======================================================
    # ===================== EXPRESSIONS ====================
    # ======================================================

    def visitExpression(self, ctx: SmallerBasicParser.ExpressionContext):
        """
        Visit Expression node in parse tree

        Parameters:
            ctx (SmallerBasicParser.ExpressionContext): The parse tree
        """
        return super().visitExpression(ctx)

    # ==================== LOGICAL AND BOOELAN EXPRESSIONS ====================

    def visitLogicalExpression(self, ctx: SmallerBasicParser.LogicalExpressionContext):
        """
        Visit LogicalExpression node in parse tree

        Parameters:
            ctx (SmallerBasicParser.LogicalExpressionContext): The parse tree
        """
        if ctx.OR(0) == None and ctx.AND(0) == None:
            return self.visit(ctx.booleanExpression(0))

        operator: str = ctx.OR(0).getText() if ctx.OR(0) else ctx.AND(0).getText()

        return LogicalExpressionNode(
            self.visit(ctx.booleanExpression(0)),
            operator,
            self.visit(ctx.booleanExpression(1))
        )

    def visitBooleanExpression(self, ctx: SmallerBasicParser.BooleanExpressionContext):
        """
        Visit BooleanExpression node in parse tree

        Parameters:
            ctx (SmallerBasicParser.BooleanExpressionContext): The parse tree
        """
        return super().visitBooleanExpression(ctx)

    def visitBooleanArithmeticalExpression(self, ctx: SmallerBasicParser.BooleanArithmeticalExpressionContext):
        """
        Visit BooleanArithmeticalExpression node in parse tree

        Parameters:
            ctx (SmallerBasicParser.BooleanArithmeticalExpressionContext): The parse tree
        """
        if (ctx.GT() == None and
            ctx.GTEQ() == None and
            ctx.LT() == None and
            ctx.LTEQ() == None and
            ctx.EQ() == None and
            ctx.NEQ() == None):
            return self.visit(ctx.arithmeticalExpression(0))

        operator: str = ctx.GT().getText() if ctx.GT() else ctx.GTEQ().getText() if ctx.GTEQ() else ctx.LT().getText() if ctx.LT() else ctx.LTEQ().getText() if ctx.LTEQ() else ctx.EQ().getText() if ctx.EQ() else ctx.NEQ().getText()

        return BooleanArithmeticalExpressionNode(
            self.visit(ctx.arithmeticalExpression(0)),
            operator,
            self.visit(ctx.arithmeticalExpression(1))
        )

    def visitBooleanStringExpression(self, ctx: SmallerBasicParser.BooleanStringExpressionContext):
        """
        Visit BooleanStringExpression node in parse tree

        Parameters:
            ctx (SmallerBasicParser.BooleanStringExpressionContext): The parse tree
        """
        if (ctx.GT() == None and
            ctx.GTEQ() == None and
            ctx.LT() == None and
            ctx.LTEQ() == None and
            ctx.EQ() == None and
            ctx.NEQ() == None):
            return self.visit(ctx.stringExpression(0))

        operator: str = ctx.GT().getText() if ctx.GT() else ctx.GTEQ().getText() if ctx.GTEQ() else ctx.LT().getText() if ctx.LT() else ctx.LTEQ().getText() if ctx.LTEQ() else ctx.EQ().getText() if ctx.EQ() else ctx.NEQ().getText()

        return BooleanStringExpressionNode(
            self.visit(ctx.stringExpression(0)),
            operator,
            self.visit(ctx.stringExpression(1))
        )

    def visitBooleanAtomExpression(self, ctx: SmallerBasicParser.BooleanAtomExpressionContext):
        """
        Visit BooleanAtomExpression node in parse tree

        Parameters:
            ctx (SmallerBasicParser.BooleanAtomExpressionContext): The parse tree
        """
        return super().visitBooleanAtomExpression(ctx)

    def visitAtomBoolean(self, ctx: SmallerBasicParser.AtomBooleanContext):
        """
        Visit AtomBoolean node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomBooleanContext): The parse tree
        """
        return super().visitAtomBoolean(ctx)

    def visitAtomBooleanBoolean(self, ctx: SmallerBasicParser.AtomBooleanBooleanContext):
        """
        Visit AtomBooleanBoolean node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomBooleanBooleanContext): The parse tree
        """
        return BooleanNode(ctx.BOOLEAN().getText())

    def visitAtomBooleanId(self, ctx: SmallerBasicParser.AtomBooleanIdContext):
        """
        Visit AtomBooleanId node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomBooleanIdContext): The parse tree
        """
        return IdNode(ctx.ID().getText())

    def visitAtomBooleanParenthesis(self, ctx: SmallerBasicParser.AtomBooleanParenthesisContext):
        """
        Visit AtomBooleanParenthesis node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomBooleanParenthesisContext): The parse tree
        """
        return self.visit(ctx.logicalExpression())

    def visitAtomBooleanLibraryStatement(self, ctx: SmallerBasicParser.AtomBooleanLibraryStatementContext):
        """
        Visit AtomBooleanLibraryStatement node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomBooleanLibraryStatementContext): The parse tree
        """
        return self.visit(ctx.libraryStatement())

    def visitAtomBooleanArrayAccess(self, ctx: SmallerBasicParser.AtomBooleanArrayAccessContext):
        """
        Visit AtomBooleanArrayAccess node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomBooleanArrayAccessContext): The parse tree
        """
        return self.visit(ctx.arrayAccess())

    # ==================== ARITHMETICAL EXPRESSIONS ====================

    def visitArithmeticalExpression(self, ctx: SmallerBasicParser.ArithmeticalExpressionContext):
        """
        Visit ArithmeticalExpression node in parse tree

        Parameters:
            ctx (SmallerBasicParser.ArithmeticalExpressionContext): The parse tree
        """
        return super().visitArithmeticalExpression(ctx)

    def visitAdditiveExpression(self, ctx: SmallerBasicParser.AdditiveExpressionContext):
        """
        Visit AdditiveExpression node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AdditiveExpressionContext): The parse tree
        """
        if ctx.PLUS(0) == None and ctx.MINUS(0) == None:
            return self.visit(ctx.multiplicativeExpression(0))

        operator: str = ctx.PLUS(0).getText() if ctx.PLUS(0) else ctx.MINUS(0).getText()

        return AdditiveExpressionNode(
            self.visit(ctx.multiplicativeExpression(0)),
            operator,
            self.visit(ctx.multiplicativeExpression(1))
        )

    def visitMultiplicativeExpression(self, ctx: SmallerBasicParser.MultiplicativeExpressionContext):
        """
        Visit MultiplicativeExpression node in parse tree

        Parameters:
            ctx (SmallerBasicParser.MultiplicativeExpressionContext): The parse tree
        """
        if ctx.MUL(0) == None and ctx.DIV(0) == None:
            return self.visit(ctx.unaryAtomNumber())

        operator: str = ctx.MUL(0).getText() if ctx.MUL(0) else ctx.DIV(0).getText()

        return MultiplicativeExpressionNode(
            self.visit(ctx.unaryAtomNumber()),
            operator,
            self.visit(ctx.multiplicativeExpression(0))
        )

    def visitUnaryAtomNumber(self, ctx: SmallerBasicParser.UnaryAtomNumberContext):
        """
        Visit UnaryAtomNumber node in parse tree

        Parameters:
            ctx (SmallerBasicParser.UnaryAtomNumberContext): The parse tree
        """
        unary_sign: str = get_unary_sign(ctx)

        if unary_sign == "":
            return self.visit(ctx.atomNumber())

        return UnaryAtomNumberNode(
            unary_sign,
            self.visit(ctx.atomNumber())
        )

    def visitAtomNumberInt(self, ctx: SmallerBasicParser.AtomNumberIntContext):
        """
        Visit AtomNumberInt node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomNumberIntContext): The parse tree
        """
        return IntNode(ctx.INT().getText())

    def visitAtomNumberFloat(self, ctx: SmallerBasicParser.AtomNumberFloatContext):
        """
        Visit AtomNumberFloat node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomNumberFloatContext): The parse tree
        """
        return FloatNode(ctx.FLOAT().getText())

    def visitAtomNumberId(self, ctx: SmallerBasicParser.AtomNumberIdContext):
        """
        Visit AtomNumberId node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomNumberIdContext): The parse tree
        """
        return IdNode(ctx.ID().getText())

    def visitAtomNumberParenthesis(self, ctx: SmallerBasicParser.AtomNumberParenthesisContext):
        """
        Visit AtomNumberParenthesis node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomNumberParenthesisContext): The parse tree
        """
        return self.visit(ctx.additiveExpression())

    def visitAtomNumberLibraryStatement(self, ctx: SmallerBasicParser.AtomNumberLibraryStatementContext):
        """
        Visit AtomNumberLibraryStatement node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomNumberLibraryStatementContext): The parse tree
        """
        return self.visit(ctx.libraryStatement())

    def visitAtomNumberArrayAccess(self, ctx: SmallerBasicParser.AtomNumberArrayAccessContext):
        """
        Visit AtomNumberArrayAccess node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomNumberArrayAccessContext): The parse tree
        """
        return self.visit(ctx.arrayAccess())

    # ==================== STRING EXPRESSIONS ====================

    def visitStringExpression(self, ctx: SmallerBasicParser.StringExpressionContext):
        """
        Visit StringExpression node in parse tree

        Parameters:
            ctx (SmallerBasicParser.StringExpressionContext): The parse tree
        """
        return super().visitStringExpression(ctx)

    def visitAdditiveStringExpression(self, ctx: SmallerBasicParser.AdditiveStringExpressionContext):
        """
        Visit AdditiveStringExpressionWithOp node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AdditiveStringExpressionWithOpContext): The parse tree
        """

        if ctx.PLUS(0) == None:
            return self.visit(ctx.atomString())

        return AdditiveStringExpressionNode(
            self.visit(ctx.atomString()),
            ctx.PLUS(0).getText(),
            self.visit(ctx.additiveStringExpression(0))
        )

    def visitAtomStringLiteral(self, ctx: SmallerBasicParser.AtomStringLiteralContext):
        """
        Visit AtomStringLiteral node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomStringLiteralContext): The parse tree
        """
        return StringNode(ctx.STRING().getText()[1:-1])

    def visitAtomStringId(self, ctx: SmallerBasicParser.AtomStringIdContext):
        """
        Visit AtomStringId node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomStringIdContext): The parse tree
        """
        return IdNode(ctx.ID().getText())

    def visitAtomStringParenthesis(self, ctx: SmallerBasicParser.AtomStringParenthesisContext):
        """
        Visit AtomStringParenthesis node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomStringParenthesisContext): The parse tree
        """
        return self.visit(ctx.stringExpression())

    def visitAtomStringLibraryStatement(self, ctx: SmallerBasicParser.AtomStringLibraryStatementContext):
        """
        Visit AtomStringLibraryStatement node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomStringLibraryStatementContext): The parse tree
        """
        return self.visit(ctx.libraryStatement())

    def visitAtomStringArrayAccess(self, ctx: SmallerBasicParser.AtomStringArrayAccessContext):
        """
        Visit AtomStringArrayAccess node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomStringArrayAccessContext): The parse tree
        """
        return self.visit(ctx.arrayAccess())
