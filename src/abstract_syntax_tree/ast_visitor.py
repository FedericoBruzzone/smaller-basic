from typing import List
from src.abstract_syntax_tree.statement_nodes.abstract_statement_node import AbstractStatementNode

from src.grammar.SmallerBasicVisitor import SmallerBasicVisitor
from src.grammar.SmallerBasicParser import SmallerBasicParser

from src.abstract_syntax_tree.ast_visitor_helper import get_unary_sign

from src.abstract_syntax_tree.ast import Ast
from src.abstract_syntax_tree.statement_nodes.abstract_statement_node import AbstractStatementNode
from src.abstract_syntax_tree.statement_nodes.varible_declaration_statement_node import VariableDeclarationStatementNode


# ======================================================
# ===================== EXPRESSIONS ====================
# ======================================================
# ==================== ARITHMETICAL EXPRESSIONS ==================== 
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.additive_expression_node import AdditiveExpressionNode
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.multiplicative_expression_node import MultiplicativeExpressionNode
from src.abstract_syntax_tree.expression_nodes.arithmetical_expression_nodes.unary_atom_number_node import UnaryAtomNumberNode
# ==================== STRING EXPRESSIONS ====================
from src.abstract_syntax_tree.expression_nodes.string_expression_nodes.additive_string_expression_node import AdditiveStringExpressionNode
# ==================== TOKENS ====================
from src.abstract_syntax_tree.token_nodes.id_node import IdNode
from src.abstract_syntax_tree.token_nodes.string_node import StringNode
from src.abstract_syntax_tree.token_nodes.int_node import IntNode
from src.abstract_syntax_tree.token_nodes.float_node import FloatNode


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

    # # ======================================================
    # # ===================== EXPRESSIONS ====================
    # # ======================================================

    def visitExpression(self, ctx: SmallerBasicParser.ExpressionContext):
        """
        Visit Expression node in parse tree

        Parameters:
            ctx (SmallerBasicParser.ExpressionContext): The parse tree
        """
        return super().visitExpression(ctx)

    # # ==================== ARITHMETICAL EXPRESSIONS ==================== 
    
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
            return self.visit(ctx.multiplicativeExpression())

        operator: str = ctx.PLUS(0).getText() if ctx.PLUS(0) else ctx.MINUS(0).getText()

        return AdditiveExpressionNode(
            self.visit(ctx.multiplicativeExpression()),
            operator,
            self.visit(ctx.additiveExpression(0))
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
        return StringNode(ctx.STRING().getText())

    def visitAtomStringId(self, ctx: SmallerBasicParser.AtomStringIdContext):
        """
        Visit AtomStringId node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomStringIdContext): The parse tree
        """
        return IdNode(ctx.ID().getText())

