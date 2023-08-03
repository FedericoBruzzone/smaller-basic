from typing import List

from src.grammar.SmallerBasicVisitor import SmallerBasicVisitor
from src.grammar.SmallerBasicParser import SmallerBasicParser 

from src.abstract_syntax_tree.ast_visitor_helper import get_unary_sign 

from src.abstract_syntax_tree.ast                                                    import Ast
from src.abstract_syntax_tree.abstract_ast_node                                      import AbstractAstNode
from src.abstract_syntax_tree.statement_nodes.varible_declaration_statement_node     import VariableDeclarationStatementNode
from src.abstract_syntax_tree.token_nodes.id_node                                    import IdNode
from src.abstract_syntax_tree.expression_nodes.literal_nodes.signed_int_literal_node import SignedIntLiteralNode

class SmallerBasicAstVisitor(SmallerBasicVisitor):
    """
    This class visits the parse tree and creates an abstract syntax tree.
    """

    def visitProgram(self, ctx: SmallerBasicParser.ProgramContext):
        """
        Visit Program node in parse tree 

        Parameters:
            ctx (SmallerBasicParser.ProgramContext): The parse tree
        """
        statements: List[AbstractAstNode] = [self.visit(child) for child in ctx.statement()]
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

    def visitExpression(self, ctx: SmallerBasicParser.ExpressionContext):
        """
        Visit Expression node in parse tree

        Parameters:
            ctx (SmallerBasicParser.ExpressionContext): The parse tree
        """
        return super().visitExpression(ctx)
    
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

         

    # def visitSignedNumber(self, ctx: SmallerBasicParser.SignedNumberContext):
    #     """
    #     Visit SignedNumber node in parse tree

    #     Parameters:
    #         ctx (SmallerBasicParser.SignedNumberContext): The parse tree
    #     """
    #     sign: str = ""
    #     if ctx.MINUS() != None:
    #         sign = "-"
    #     if ctx.PLUS() != None:
    #         sign = "+"
        
    #     print(sign)
    #     print(ctx.NUMBER_LITERAL())

    #     return AbstractAstNode()
