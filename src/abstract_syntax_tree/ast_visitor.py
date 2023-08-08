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
# ==================== TOKENS ====================
from src.abstract_syntax_tree.token_nodes.id_node import IdNode
from src.abstract_syntax_tree.token_nodes.string_node import StringNode
from src.abstract_syntax_tree.token_nodes.int_node import IntNode
from src.abstract_syntax_tree.token_nodes.float_node import FloatNode
from src.abstract_syntax_tree.token_nodes.boolean_node import BooleanNode


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
 
 # AtomBooleanId                  
 # AtomBooleanParenthesis
 # AtomBooleanLibraryStatement

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

    def visitAtomStringParenthesis(self, ctx: SmallerBasicParser.AtomStringParenthesisContext):
        """
        Visit AtomStringParenthesis node in parse tree

        Parameters:
            ctx (SmallerBasicParser.AtomStringParenthesisContext): The parse tree
        """
        return self.visit(ctx.stringExpression())

