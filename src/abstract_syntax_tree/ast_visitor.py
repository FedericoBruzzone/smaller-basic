from typing import List
from src.abstract_syntax_tree.statement_nodes.abstract_statement_node import AbstractStatementNode

from src.grammar.SmallerBasicVisitor import SmallerBasicVisitor
from src.grammar.SmallerBasicParser import SmallerBasicParser

from src.abstract_syntax_tree.ast_visitor_helper import get_unary_sign

from src.abstract_syntax_tree.ast import Ast
from src.abstract_syntax_tree.statement_nodes.abstract_statement_node import AbstractStatementNode
from src.abstract_syntax_tree.statement_nodes.varible_declaration_statement_node import VariableDeclarationStatementNode
from src.abstract_syntax_tree.token_nodes.id_node import IdNode


# ======================================================
# ===================== EXPRESSIONS ====================
# ======================================================
# ==================== ARITHMETICAL EXPRESSIONS ==================== 
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.additive_expression_node import AdditiveExpressionNode
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.multiplicative_expression_node import MultiplicativeExpressionNode
# ==================== STRING EXPRESSIONS ====================
from src.abstract_syntax_tree.expression_nodes.string_expression_nodes.additive_string_expression_node import AdditiveStringExpressionNode
# ==================== LITERAL ====================
from src.abstract_syntax_tree.expression_nodes.literal_nodes.signed_int_literal_node import SignedIntLiteralNode
from src.abstract_syntax_tree.expression_nodes.literal_nodes.signed_float_literal_node import SignedFloatLiteralNode
from src.abstract_syntax_tree.expression_nodes.literal_nodes.string_literal_node import StringLiteralNode
from src.abstract_syntax_tree.expression_nodes.literal_nodes.boolean_literal_node import BooleanLiteralNode
from src.abstract_syntax_tree.expression_nodes.literal_nodes.signed_id_literal_node import SignedIdLiteralNode


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

    def visitStatement(self, ctx: SmallerBasicParser.StatementContext):
        """
        Visit Statement node in parse tree

        Parameters:
            ctx (SmallerBasicParser.StatementContext): The parse tree
        """
        return super().visitStatement(ctx)

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
            return AdditiveExpressionNode(
                self.visit(ctx.multiplicativeExpression(0)),
                None,
                None
            )
        operator: str = ctx.PLUS(0).getText() if ctx.PLUS(0) else ctx.MINUS(0).getText()
        print(operator)
        return AdditiveExpressionNode(
            self.visit(ctx.multiplicativeExpression(0)),
            operator,
            self.visit(ctx.multiplicativeExpression(1)),
        )

    def visitMultiplicativeExpression(self, ctx: SmallerBasicParser.MultiplicativeExpressionContext):
        """
        Visit MultiplicativeExpression node in parse tree

        Parameters:
            ctx (SmallerBasicParser.MultiplicativeExpressionContext): The parse tree
        """
        if ctx.MUL(0) == None and ctx.DIV(0) == None:
            return MultiplicativeExpressionNode(
                self.visit(ctx.atomNumber()),
                None,
                None
            )
        operator: str = ctx.MUL(0).getText() if ctx.MUL(0) else ctx.DIV(0).getText()
        return MultiplicativeExpressionNode(
            self.visit(ctx.atomNumber()),
            operator,
            self.visit(ctx.multiplicativeExpression(0))
        )

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
            return AdditiveStringExpressionNode(
                self.visit(ctx.atomString()),
                None,
                None
            )
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
        return self.visit(ctx.string()) 

    def visitAtomStringId(self, ctx: SmallerBasicParser.AtomStringIdContext):
        """
        Visit AtomStringId node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomStringIdContext): The parse tree
        """
        return IdNode(ctx.ID().getText())

    # ==================== LITERAL ====================

    def visitLiteral(self, ctx: SmallerBasicParser.LiteralContext):
        """
        Visit Literal node in parse tree

        Parameters:
            ctx (SmallerBasicParser.LiteralContext): The parse tree
        """
        return super().visitLiteral(ctx)

    def visitSignedInt(self, ctx: SmallerBasicParser.SignedIntContext):
        """
        Visit SignedInt node in parse tree

        Parameters:
            ctx (SmallerBasicParser.SignedIntContext): The parse tree
        """
        return SignedIntLiteralNode(
            get_unary_sign(ctx),
            ctx.INT().getText()
        )

    def visitSignedFloat(self, ctx: SmallerBasicParser.SignedFloatContext):
        """
        Visit SignedFloat node in parse tree

        Parameters:
            ctx (SmallerBasicParser.SignedFloatContext): The parse tree
        """
        return SignedFloatLiteralNode(
            get_unary_sign(ctx),
            ctx.FLOAT().getText()
        )

    def visitString(self, ctx: SmallerBasicParser.StringContext):
        """
        Visit String node in parse tree

        Parameters:
            ctx (SmallerBasicParser.StringContext): The parse tree
        """
        return StringLiteralNode(ctx.STRING_LITERAL().getText())

    def visitBoolean(self, ctx: SmallerBasicParser.BooleanContext):
        """
        Visit Boolean node in parse tree

        Parameters:
            ctx (SmallerBasicParser.BooleanContext): The parse tree
        """
        return BooleanLiteralNode(ctx.BOOLEAN_LITERAL().getText())

    def visitSignedId(self, ctx: SmallerBasicParser.SignedIdContext):
        """
        Visit SignedId node in parse tree

        Parameters:
            ctx (SmallerBasicParser.SignedIdContext): The parse tree
        """
        return SignedIdLiteralNode(
            get_unary_sign(ctx),
            ctx.ID().getText()
        )
