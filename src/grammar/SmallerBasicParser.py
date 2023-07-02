# Generated from src/grammar/SmallerBasic.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,24,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,2,1,2,1,2,1,2,3,2,20,8,2,1,2,1,2,1,2,0,0,3,0,2,4,0,
        0,22,0,7,1,0,0,0,2,13,1,0,0,0,4,15,1,0,0,0,6,8,3,4,2,0,7,6,1,0,0,
        0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,12,5,0,0,
        1,12,1,1,0,0,0,13,14,5,4,0,0,14,3,1,0,0,0,15,16,5,1,0,0,16,19,5,
        10,0,0,17,18,5,2,0,0,18,20,3,2,1,0,19,17,1,0,0,0,19,20,1,0,0,0,20,
        21,1,0,0,0,21,22,5,3,0,0,22,5,1,0,0,0,2,9,19
    ]

class SmallerBasicParser ( Parser ):

    grammarFileName = "SmallerBasic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'='", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUM", "FLOAT", "INT", "EXPONENT", "NUMBER", "SIGN", 
                      "ID", "LETTER", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_statement = 2

    ruleNames =  [ "program", "expression", "statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    NUM=4
    FLOAT=5
    INT=6
    EXPONENT=7
    NUMBER=8
    SIGN=9
    ID=10
    LETTER=11
    WS=12
    COMMENT=13
    LINE_COMMENT=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SmallerBasicParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.StatementContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.StatementContext,i)


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SmallerBasicParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.statement()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 11
            self.match(SmallerBasicParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(SmallerBasicParser.NUM, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = SmallerBasicParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(SmallerBasicParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VariableDeclarationStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(SmallerBasicParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarationStatement" ):
                listener.enterVariableDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarationStatement" ):
                listener.exitVariableDeclarationStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarationStatement" ):
                return visitor.visitVariableDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = SmallerBasicParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        self._la = 0 # Token type
        try:
            localctx = SmallerBasicParser.VariableDeclarationStatementContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(SmallerBasicParser.T__0)
            self.state = 16
            self.match(SmallerBasicParser.ID)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 17
                self.match(SmallerBasicParser.T__1)
                self.state = 18
                self.expression()


            self.state = 21
            self.match(SmallerBasicParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





