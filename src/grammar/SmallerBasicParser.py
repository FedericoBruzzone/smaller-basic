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
        4,1,27,64,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,3,1,3,1,3,5,3,37,8,3,10,3,12,3,40,9,3,
        1,4,1,4,1,4,5,4,45,8,4,10,4,12,4,48,9,4,1,5,1,5,1,5,5,5,53,8,5,10,
        5,12,5,56,9,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,
        14,16,0,5,1,0,6,7,1,0,8,9,2,0,2,2,17,17,2,0,1,1,17,17,1,0,1,3,59,
        0,19,1,0,0,0,2,25,1,0,0,0,4,31,1,0,0,0,6,33,1,0,0,0,8,41,1,0,0,0,
        10,49,1,0,0,0,12,57,1,0,0,0,14,59,1,0,0,0,16,61,1,0,0,0,18,20,3,
        2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,
        23,1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,26,5,17,0,0,26,27,5,12,
        0,0,27,29,3,4,2,0,28,30,5,26,0,0,29,28,1,0,0,0,29,30,1,0,0,0,30,
        3,1,0,0,0,31,32,3,8,4,0,32,5,1,0,0,0,33,38,3,12,6,0,34,35,5,6,0,
        0,35,37,3,12,6,0,36,34,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,
        1,0,0,0,39,7,1,0,0,0,40,38,1,0,0,0,41,46,3,10,5,0,42,43,7,0,0,0,
        43,45,3,10,5,0,44,42,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,
        0,0,0,47,9,1,0,0,0,48,46,1,0,0,0,49,54,3,14,7,0,50,51,7,1,0,0,51,
        53,3,14,7,0,52,50,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,
        0,0,55,11,1,0,0,0,56,54,1,0,0,0,57,58,7,2,0,0,58,13,1,0,0,0,59,60,
        7,3,0,0,60,15,1,0,0,0,61,62,7,4,0,0,62,17,1,0,0,0,5,21,29,38,46,
        54
    ]

class SmallerBasicParser ( Parser ):

    grammarFileName = "SmallerBasic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", 
                     "'='", "'>='", "'<='", "'<>'" ]

    symbolicNames = [ "<INVALID>", "NUMBER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "LPAREN", "RPAREN", "PLUS", "MINUS", "MUL", "DIV", 
                      "GT", "LT", "EQ", "GTEQ", "LTEQ", "NEQ", "RELATIONAL_OPERATOR", 
                      "ID", "INT", "FLOAT", "EXPONENT", "SIGN", "NUM", "CHAR", 
                      "WS", "COMMENT", "NEWLINE", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_additiveStringExpression = 3
    RULE_additiveExpression = 4
    RULE_multiplicativeExpression = 5
    RULE_atomString = 6
    RULE_atom = 7
    RULE_literal = 8

    ruleNames =  [ "program", "statement", "expression", "additiveStringExpression", 
                   "additiveExpression", "multiplicativeExpression", "atomString", 
                   "atom", "literal" ]

    EOF = Token.EOF
    NUMBER_LITERAL=1
    STRING_LITERAL=2
    BOOLEAN_LITERAL=3
    LPAREN=4
    RPAREN=5
    PLUS=6
    MINUS=7
    MUL=8
    DIV=9
    GT=10
    LT=11
    EQ=12
    GTEQ=13
    LTEQ=14
    NEQ=15
    RELATIONAL_OPERATOR=16
    ID=17
    INT=18
    FLOAT=19
    EXPONENT=20
    SIGN=21
    NUM=22
    CHAR=23
    WS=24
    COMMENT=25
    NEWLINE=26
    LINE_COMMENT=27

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
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==17):
                    break

            self.state = 23
            self.match(SmallerBasicParser.EOF)
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

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)

        def EQ(self):
            return self.getToken(SmallerBasicParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(SmallerBasicParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(SmallerBasicParser.NEWLINE, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SmallerBasicParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(SmallerBasicParser.ID)
            self.state = 26
            self.match(SmallerBasicParser.EQ)
            self.state = 27
            self.expression()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 28
                self.match(SmallerBasicParser.NEWLINE)


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

        def additiveExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.AdditiveExpressionContext,0)


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
        self.enterRule(localctx, 4, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.additiveExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveStringExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomString(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.AtomStringContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.AtomStringContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(SmallerBasicParser.PLUS)
            else:
                return self.getToken(SmallerBasicParser.PLUS, i)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_additiveStringExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveStringExpression" ):
                listener.enterAdditiveStringExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveStringExpression" ):
                listener.exitAdditiveStringExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveStringExpression" ):
                return visitor.visitAdditiveStringExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveStringExpression(self):

        localctx = SmallerBasicParser.AdditiveStringExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_additiveStringExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.atomString()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 34
                self.match(SmallerBasicParser.PLUS)
                self.state = 35
                self.atomString()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(SmallerBasicParser.PLUS)
            else:
                return self.getToken(SmallerBasicParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(SmallerBasicParser.MINUS)
            else:
                return self.getToken(SmallerBasicParser.MINUS, i)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = SmallerBasicParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.multiplicativeExpression()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 42
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 43
                self.multiplicativeExpression()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.AtomContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.AtomContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(SmallerBasicParser.MUL)
            else:
                return self.getToken(SmallerBasicParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(SmallerBasicParser.DIV)
            else:
                return self.getToken(SmallerBasicParser.DIV, i)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = SmallerBasicParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.atom()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 50
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 51
                self.atom()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(SmallerBasicParser.STRING_LITERAL, 0)

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_atomString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomString" ):
                listener.enterAtomString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomString" ):
                listener.exitAtomString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomString" ):
                return visitor.visitAtomString(self)
            else:
                return visitor.visitChildren(self)




    def atomString(self):

        localctx = SmallerBasicParser.AtomStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atomString)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            _la = self._input.LA(1)
            if not(_la==2 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LITERAL(self):
            return self.getToken(SmallerBasicParser.NUMBER_LITERAL, 0)

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = SmallerBasicParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not(_la==1 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LITERAL(self):
            return self.getToken(SmallerBasicParser.NUMBER_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(SmallerBasicParser.STRING_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(SmallerBasicParser.BOOLEAN_LITERAL, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = SmallerBasicParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





