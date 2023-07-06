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
        4,1,22,151,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,4,0,40,8,0,
        11,0,12,0,41,1,0,1,0,1,1,1,1,1,2,1,2,1,2,3,2,51,8,2,1,2,3,2,54,8,
        2,1,3,1,3,1,3,1,3,3,3,60,8,3,1,4,1,4,1,4,4,4,65,8,4,11,4,12,4,66,
        1,4,3,4,70,8,4,1,5,1,5,1,5,1,5,1,5,3,5,77,8,5,1,6,1,6,1,6,1,6,1,
        6,1,6,3,6,85,8,6,1,7,1,7,1,8,1,8,1,8,4,8,92,8,8,11,8,12,8,93,1,8,
        3,8,97,8,8,1,9,1,9,1,9,4,9,102,8,9,11,9,12,9,103,1,9,3,9,107,8,9,
        1,10,1,10,1,10,1,10,1,10,1,10,3,10,115,8,10,1,11,1,11,1,12,1,12,
        1,12,5,12,122,8,12,10,12,12,12,125,9,12,1,13,1,13,3,13,129,8,13,
        1,14,1,14,1,14,1,14,3,14,135,8,14,1,15,3,15,138,8,15,1,15,1,15,1,
        16,1,16,1,17,1,17,1,18,3,18,147,8,18,1,18,1,18,1,18,0,0,19,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,4,1,0,16,17,1,0,
        10,15,1,0,6,7,1,0,8,9,155,0,39,1,0,0,0,2,45,1,0,0,0,4,47,1,0,0,0,
        6,59,1,0,0,0,8,69,1,0,0,0,10,76,1,0,0,0,12,84,1,0,0,0,14,86,1,0,
        0,0,16,96,1,0,0,0,18,106,1,0,0,0,20,114,1,0,0,0,22,116,1,0,0,0,24,
        118,1,0,0,0,26,128,1,0,0,0,28,134,1,0,0,0,30,137,1,0,0,0,32,141,
        1,0,0,0,34,143,1,0,0,0,36,146,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,
        0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,43,44,
        5,0,0,1,44,1,1,0,0,0,45,46,3,4,2,0,46,3,1,0,0,0,47,50,5,18,0,0,48,
        49,5,12,0,0,49,51,3,6,3,0,50,48,1,0,0,0,50,51,1,0,0,0,51,53,1,0,
        0,0,52,54,5,21,0,0,53,52,1,0,0,0,53,54,1,0,0,0,54,5,1,0,0,0,55,60,
        3,14,7,0,56,60,3,8,4,0,57,60,3,22,11,0,58,60,3,28,14,0,59,55,1,0,
        0,0,59,56,1,0,0,0,59,57,1,0,0,0,59,58,1,0,0,0,60,7,1,0,0,0,61,64,
        3,10,5,0,62,63,7,0,0,0,63,65,3,10,5,0,64,62,1,0,0,0,65,66,1,0,0,
        0,66,64,1,0,0,0,66,67,1,0,0,0,67,70,1,0,0,0,68,70,3,10,5,0,69,61,
        1,0,0,0,69,68,1,0,0,0,70,9,1,0,0,0,71,72,3,14,7,0,72,73,7,1,0,0,
        73,74,3,14,7,0,74,77,1,0,0,0,75,77,3,12,6,0,76,71,1,0,0,0,76,75,
        1,0,0,0,77,11,1,0,0,0,78,85,3,34,17,0,79,85,3,36,18,0,80,81,5,4,
        0,0,81,82,3,8,4,0,82,83,5,5,0,0,83,85,1,0,0,0,84,78,1,0,0,0,84,79,
        1,0,0,0,84,80,1,0,0,0,85,13,1,0,0,0,86,87,3,16,8,0,87,15,1,0,0,0,
        88,91,3,18,9,0,89,90,7,2,0,0,90,92,3,18,9,0,91,89,1,0,0,0,92,93,
        1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,97,1,0,0,0,95,97,3,18,9,0,
        96,88,1,0,0,0,96,95,1,0,0,0,97,17,1,0,0,0,98,101,3,20,10,0,99,100,
        7,3,0,0,100,102,3,20,10,0,101,99,1,0,0,0,102,103,1,0,0,0,103,101,
        1,0,0,0,103,104,1,0,0,0,104,107,1,0,0,0,105,107,3,20,10,0,106,98,
        1,0,0,0,106,105,1,0,0,0,107,19,1,0,0,0,108,115,3,30,15,0,109,115,
        3,36,18,0,110,111,5,4,0,0,111,112,3,14,7,0,112,113,5,5,0,0,113,115,
        1,0,0,0,114,108,1,0,0,0,114,109,1,0,0,0,114,110,1,0,0,0,115,21,1,
        0,0,0,116,117,3,24,12,0,117,23,1,0,0,0,118,123,3,26,13,0,119,120,
        5,6,0,0,120,122,3,26,13,0,121,119,1,0,0,0,122,125,1,0,0,0,123,121,
        1,0,0,0,123,124,1,0,0,0,124,25,1,0,0,0,125,123,1,0,0,0,126,129,3,
        32,16,0,127,129,3,36,18,0,128,126,1,0,0,0,128,127,1,0,0,0,129,27,
        1,0,0,0,130,135,3,30,15,0,131,135,3,32,16,0,132,135,3,34,17,0,133,
        135,3,36,18,0,134,130,1,0,0,0,134,131,1,0,0,0,134,132,1,0,0,0,134,
        133,1,0,0,0,135,29,1,0,0,0,136,138,7,2,0,0,137,136,1,0,0,0,137,138,
        1,0,0,0,138,139,1,0,0,0,139,140,5,1,0,0,140,31,1,0,0,0,141,142,5,
        2,0,0,142,33,1,0,0,0,143,144,5,3,0,0,144,35,1,0,0,0,145,147,7,2,
        0,0,146,145,1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,149,5,18,
        0,0,149,37,1,0,0,0,18,41,50,53,59,66,69,76,84,93,96,103,106,114,
        123,128,134,137,146
    ]

class SmallerBasicParser ( Parser ):

    grammarFileName = "SmallerBasic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", 
                     "'='", "'>='", "'<='", "'<>'", "'And'", "'Or'" ]

    symbolicNames = [ "<INVALID>", "NUMBER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "LPAREN", "RPAREN", "PLUS", "MINUS", "MUL", "DIV", 
                      "GT", "LT", "EQ", "GTEQ", "LTEQ", "NEQ", "AND", "OR", 
                      "ID", "WS", "COMMENT", "NEWLINE", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declarationStatement = 2
    RULE_expression = 3
    RULE_logicalExpression = 4
    RULE_booleanExpression = 5
    RULE_atomBoolean = 6
    RULE_arithmeticalExpression = 7
    RULE_additiveExpression = 8
    RULE_multiplicativeExpression = 9
    RULE_atomNumber = 10
    RULE_stringExpression = 11
    RULE_additiveStringExpression = 12
    RULE_atomString = 13
    RULE_literal = 14
    RULE_signedNumber = 15
    RULE_string = 16
    RULE_boolean = 17
    RULE_id = 18

    ruleNames =  [ "program", "statement", "declarationStatement", "expression", 
                   "logicalExpression", "booleanExpression", "atomBoolean", 
                   "arithmeticalExpression", "additiveExpression", "multiplicativeExpression", 
                   "atomNumber", "stringExpression", "additiveStringExpression", 
                   "atomString", "literal", "signedNumber", "string", "boolean", 
                   "id" ]

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
    AND=16
    OR=17
    ID=18
    WS=19
    COMMENT=20
    NEWLINE=21
    LINE_COMMENT=22

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
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.statement()
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==18):
                    break

            self.state = 43
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

        def declarationStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.DeclarationStatementContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.declarationStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementContext(ParserRuleContext):
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
            return SmallerBasicParser.RULE_declarationStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatement" ):
                listener.enterDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatement" ):
                listener.exitDeclarationStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationStatement" ):
                return visitor.visitDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)




    def declarationStatement(self):

        localctx = SmallerBasicParser.DeclarationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declarationStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(SmallerBasicParser.ID)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 48
                self.match(SmallerBasicParser.EQ)
                self.state = 49
                self.expression()


            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 52
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

        def arithmeticalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.ArithmeticalExpressionContext,0)


        def logicalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.LogicalExpressionContext,0)


        def stringExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.StringExpressionContext,0)


        def literal(self):
            return self.getTypedRuleContext(SmallerBasicParser.LiteralContext,0)


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
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.arithmeticalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.logicalExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.stringExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def booleanExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.BooleanExpressionContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.BooleanExpressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(SmallerBasicParser.AND)
            else:
                return self.getToken(SmallerBasicParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(SmallerBasicParser.OR)
            else:
                return self.getToken(SmallerBasicParser.OR, i)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_logicalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpression" ):
                listener.enterLogicalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpression" ):
                listener.exitLogicalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpression" ):
                return visitor.visitLogicalExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalExpression(self):

        localctx = SmallerBasicParser.LogicalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_logicalExpression)
        self._la = 0 # Token type
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.booleanExpression()
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 62
                    _la = self._input.LA(1)
                    if not(_la==16 or _la==17):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 63
                    self.booleanExpression()
                    self.state = 66 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==16 or _la==17):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.booleanExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmeticalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.ArithmeticalExpressionContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.ArithmeticalExpressionContext,i)


        def GT(self):
            return self.getToken(SmallerBasicParser.GT, 0)

        def LT(self):
            return self.getToken(SmallerBasicParser.LT, 0)

        def EQ(self):
            return self.getToken(SmallerBasicParser.EQ, 0)

        def GTEQ(self):
            return self.getToken(SmallerBasicParser.GTEQ, 0)

        def LTEQ(self):
            return self.getToken(SmallerBasicParser.LTEQ, 0)

        def NEQ(self):
            return self.getToken(SmallerBasicParser.NEQ, 0)

        def atomBoolean(self):
            return self.getTypedRuleContext(SmallerBasicParser.AtomBooleanContext,0)


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_booleanExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanExpression" ):
                listener.enterBooleanExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanExpression" ):
                listener.exitBooleanExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanExpression" ):
                return visitor.visitBooleanExpression(self)
            else:
                return visitor.visitChildren(self)




    def booleanExpression(self):

        localctx = SmallerBasicParser.BooleanExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_booleanExpression)
        self._la = 0 # Token type
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.arithmeticalExpression()
                self.state = 72
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64512) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 73
                self.arithmeticalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.atomBoolean()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomBooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean(self):
            return self.getTypedRuleContext(SmallerBasicParser.BooleanContext,0)


        def id_(self):
            return self.getTypedRuleContext(SmallerBasicParser.IdContext,0)


        def LPAREN(self):
            return self.getToken(SmallerBasicParser.LPAREN, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.LogicalExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SmallerBasicParser.RPAREN, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_atomBoolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomBoolean" ):
                listener.enterAtomBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomBoolean" ):
                listener.exitAtomBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomBoolean" ):
                return visitor.visitAtomBoolean(self)
            else:
                return visitor.visitChildren(self)




    def atomBoolean(self):

        localctx = SmallerBasicParser.AtomBooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atomBoolean)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.boolean()
                pass
            elif token in [6, 7, 18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.id_()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.match(SmallerBasicParser.LPAREN)
                self.state = 81
                self.logicalExpression()
                self.state = 82
                self.match(SmallerBasicParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.AdditiveExpressionContext,0)


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_arithmeticalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticalExpression" ):
                listener.enterArithmeticalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticalExpression" ):
                listener.exitArithmeticalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticalExpression" ):
                return visitor.visitArithmeticalExpression(self)
            else:
                return visitor.visitChildren(self)




    def arithmeticalExpression(self):

        localctx = SmallerBasicParser.ArithmeticalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arithmeticalExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.additiveExpression()
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
        self.enterRule(localctx, 16, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.multiplicativeExpression()
                self.state = 91 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 89
                    _la = self._input.LA(1)
                    if not(_la==6 or _la==7):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 90
                    self.multiplicativeExpression()
                    self.state = 93 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==6 or _la==7):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.multiplicativeExpression()
                pass


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

        def atomNumber(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.AtomNumberContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.AtomNumberContext,i)


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
        self.enterRule(localctx, 18, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.atomNumber()
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 99
                    _la = self._input.LA(1)
                    if not(_la==8 or _la==9):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 100
                    self.atomNumber()
                    self.state = 103 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==8 or _la==9):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.atomNumber()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signedNumber(self):
            return self.getTypedRuleContext(SmallerBasicParser.SignedNumberContext,0)


        def id_(self):
            return self.getTypedRuleContext(SmallerBasicParser.IdContext,0)


        def LPAREN(self):
            return self.getToken(SmallerBasicParser.LPAREN, 0)

        def arithmeticalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.ArithmeticalExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SmallerBasicParser.RPAREN, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_atomNumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomNumber" ):
                listener.enterAtomNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomNumber" ):
                listener.exitAtomNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomNumber" ):
                return visitor.visitAtomNumber(self)
            else:
                return visitor.visitChildren(self)




    def atomNumber(self):

        localctx = SmallerBasicParser.AtomNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_atomNumber)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.signedNumber()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.id_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.match(SmallerBasicParser.LPAREN)
                self.state = 111
                self.arithmeticalExpression()
                self.state = 112
                self.match(SmallerBasicParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveStringExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.AdditiveStringExpressionContext,0)


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_stringExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpression" ):
                listener.enterStringExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpression" ):
                listener.exitStringExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpression" ):
                return visitor.visitStringExpression(self)
            else:
                return visitor.visitChildren(self)




    def stringExpression(self):

        localctx = SmallerBasicParser.StringExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_stringExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.additiveStringExpression()
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
        self.enterRule(localctx, 24, self.RULE_additiveStringExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.atomString()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 119
                self.match(SmallerBasicParser.PLUS)
                self.state = 120
                self.atomString()
                self.state = 125
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

        def string(self):
            return self.getTypedRuleContext(SmallerBasicParser.StringContext,0)


        def id_(self):
            return self.getTypedRuleContext(SmallerBasicParser.IdContext,0)


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
        self.enterRule(localctx, 26, self.RULE_atomString)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.string()
                pass
            elif token in [6, 7, 18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

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

        def signedNumber(self):
            return self.getTypedRuleContext(SmallerBasicParser.SignedNumberContext,0)


        def string(self):
            return self.getTypedRuleContext(SmallerBasicParser.StringContext,0)


        def boolean(self):
            return self.getTypedRuleContext(SmallerBasicParser.BooleanContext,0)


        def id_(self):
            return self.getTypedRuleContext(SmallerBasicParser.IdContext,0)


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
        self.enterRule(localctx, 28, self.RULE_literal)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.signedNumber()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.string()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.boolean()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 133
                self.id_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignedNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LITERAL(self):
            return self.getToken(SmallerBasicParser.NUMBER_LITERAL, 0)

        def MINUS(self):
            return self.getToken(SmallerBasicParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(SmallerBasicParser.PLUS, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_signedNumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignedNumber" ):
                listener.enterSignedNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignedNumber" ):
                listener.exitSignedNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignedNumber" ):
                return visitor.visitSignedNumber(self)
            else:
                return visitor.visitChildren(self)




    def signedNumber(self):

        localctx = SmallerBasicParser.SignedNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_signedNumber)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==7:
                self.state = 136
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 139
            self.match(SmallerBasicParser.NUMBER_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(SmallerBasicParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = SmallerBasicParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(SmallerBasicParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN_LITERAL(self):
            return self.getToken(SmallerBasicParser.BOOLEAN_LITERAL, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_boolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)




    def boolean(self):

        localctx = SmallerBasicParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_boolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(SmallerBasicParser.BOOLEAN_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)

        def MINUS(self):
            return self.getToken(SmallerBasicParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(SmallerBasicParser.PLUS, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)




    def id_(self):

        localctx = SmallerBasicParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==7:
                self.state = 145
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 148
            self.match(SmallerBasicParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





