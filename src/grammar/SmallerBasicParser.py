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
        4,1,28,187,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,4,0,44,8,0,11,0,12,0,45,1,0,1,0,1,1,1,1,1,1,3,1,53,8,1,
        1,2,1,2,1,2,3,2,58,8,2,1,2,3,2,61,8,2,1,3,1,3,1,3,1,3,1,3,3,3,68,
        8,3,1,3,4,3,71,8,3,11,3,12,3,72,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,
        3,4,83,8,4,1,4,4,4,86,8,4,11,4,12,4,87,1,4,1,4,1,5,1,5,1,5,1,5,3,
        5,96,8,5,1,6,1,6,1,6,4,6,101,8,6,11,6,12,6,102,1,6,3,6,106,8,6,1,
        7,1,7,1,7,1,7,1,7,3,7,113,8,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,121,8,
        8,1,9,1,9,1,10,1,10,1,10,4,10,128,8,10,11,10,12,10,129,1,10,3,10,
        133,8,10,1,11,1,11,1,11,4,11,138,8,11,11,11,12,11,139,1,11,3,11,
        143,8,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,151,8,12,1,13,1,13,1,
        14,1,14,1,14,5,14,158,8,14,10,14,12,14,161,9,14,1,15,1,15,3,15,165,
        8,15,1,16,1,16,1,16,1,16,3,16,171,8,16,1,17,3,17,174,8,17,1,17,1,
        17,1,18,1,18,1,19,1,19,1,20,3,20,183,8,20,1,20,1,20,1,20,0,0,21,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,4,1,
        0,16,17,1,0,10,15,1,0,6,7,1,0,8,9,195,0,43,1,0,0,0,2,52,1,0,0,0,
        4,54,1,0,0,0,6,62,1,0,0,0,8,76,1,0,0,0,10,95,1,0,0,0,12,105,1,0,
        0,0,14,112,1,0,0,0,16,120,1,0,0,0,18,122,1,0,0,0,20,132,1,0,0,0,
        22,142,1,0,0,0,24,150,1,0,0,0,26,152,1,0,0,0,28,154,1,0,0,0,30,164,
        1,0,0,0,32,170,1,0,0,0,34,173,1,0,0,0,36,177,1,0,0,0,38,179,1,0,
        0,0,40,182,1,0,0,0,42,44,3,2,1,0,43,42,1,0,0,0,44,45,1,0,0,0,45,
        43,1,0,0,0,45,46,1,0,0,0,46,47,1,0,0,0,47,48,5,0,0,1,48,1,1,0,0,
        0,49,53,3,4,2,0,50,53,3,6,3,0,51,53,3,8,4,0,52,49,1,0,0,0,52,50,
        1,0,0,0,52,51,1,0,0,0,53,3,1,0,0,0,54,57,5,24,0,0,55,56,5,12,0,0,
        56,58,3,10,5,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,61,5,
        27,0,0,60,59,1,0,0,0,60,61,1,0,0,0,61,5,1,0,0,0,62,63,5,22,0,0,63,
        64,5,4,0,0,64,65,3,12,6,0,65,67,5,5,0,0,66,68,5,27,0,0,67,66,1,0,
        0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,71,3,2,1,0,70,69,1,0,0,0,71,72,
        1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,75,5,23,0,0,
        75,7,1,0,0,0,76,77,5,18,0,0,77,78,5,4,0,0,78,79,3,12,6,0,79,80,5,
        5,0,0,80,82,5,19,0,0,81,83,5,27,0,0,82,81,1,0,0,0,82,83,1,0,0,0,
        83,85,1,0,0,0,84,86,3,2,1,0,85,84,1,0,0,0,86,87,1,0,0,0,87,85,1,
        0,0,0,87,88,1,0,0,0,88,89,1,0,0,0,89,90,5,21,0,0,90,9,1,0,0,0,91,
        96,3,18,9,0,92,96,3,12,6,0,93,96,3,26,13,0,94,96,3,32,16,0,95,91,
        1,0,0,0,95,92,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,96,11,1,0,0,0,
        97,100,3,14,7,0,98,99,7,0,0,0,99,101,3,14,7,0,100,98,1,0,0,0,101,
        102,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,106,1,0,0,0,104,
        106,3,14,7,0,105,97,1,0,0,0,105,104,1,0,0,0,106,13,1,0,0,0,107,108,
        3,18,9,0,108,109,7,1,0,0,109,110,3,18,9,0,110,113,1,0,0,0,111,113,
        3,16,8,0,112,107,1,0,0,0,112,111,1,0,0,0,113,15,1,0,0,0,114,121,
        3,38,19,0,115,121,3,40,20,0,116,117,5,4,0,0,117,118,3,12,6,0,118,
        119,5,5,0,0,119,121,1,0,0,0,120,114,1,0,0,0,120,115,1,0,0,0,120,
        116,1,0,0,0,121,17,1,0,0,0,122,123,3,20,10,0,123,19,1,0,0,0,124,
        127,3,22,11,0,125,126,7,2,0,0,126,128,3,22,11,0,127,125,1,0,0,0,
        128,129,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,133,1,0,0,0,
        131,133,3,22,11,0,132,124,1,0,0,0,132,131,1,0,0,0,133,21,1,0,0,0,
        134,137,3,24,12,0,135,136,7,3,0,0,136,138,3,24,12,0,137,135,1,0,
        0,0,138,139,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,143,1,0,
        0,0,141,143,3,24,12,0,142,134,1,0,0,0,142,141,1,0,0,0,143,23,1,0,
        0,0,144,151,3,34,17,0,145,151,3,40,20,0,146,147,5,4,0,0,147,148,
        3,18,9,0,148,149,5,5,0,0,149,151,1,0,0,0,150,144,1,0,0,0,150,145,
        1,0,0,0,150,146,1,0,0,0,151,25,1,0,0,0,152,153,3,28,14,0,153,27,
        1,0,0,0,154,159,3,30,15,0,155,156,5,6,0,0,156,158,3,30,15,0,157,
        155,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,
        29,1,0,0,0,161,159,1,0,0,0,162,165,3,36,18,0,163,165,3,40,20,0,164,
        162,1,0,0,0,164,163,1,0,0,0,165,31,1,0,0,0,166,171,3,34,17,0,167,
        171,3,36,18,0,168,171,3,38,19,0,169,171,3,40,20,0,170,166,1,0,0,
        0,170,167,1,0,0,0,170,168,1,0,0,0,170,169,1,0,0,0,171,33,1,0,0,0,
        172,174,7,2,0,0,173,172,1,0,0,0,173,174,1,0,0,0,174,175,1,0,0,0,
        175,176,5,1,0,0,176,35,1,0,0,0,177,178,5,2,0,0,178,37,1,0,0,0,179,
        180,5,3,0,0,180,39,1,0,0,0,181,183,7,2,0,0,182,181,1,0,0,0,182,183,
        1,0,0,0,183,184,1,0,0,0,184,185,5,24,0,0,185,41,1,0,0,0,23,45,52,
        57,60,67,72,82,87,95,102,105,112,120,129,132,139,142,150,159,164,
        170,173,182
    ]

class SmallerBasicParser ( Parser ):

    grammarFileName = "SmallerBasic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", 
                     "'='", "'>='", "'<='", "'<>'", "'And'", "'Or'", "'If'", 
                     "'Then'", "'Else'", "'EndIf'", "'While'", "'EndWhile'" ]

    symbolicNames = [ "<INVALID>", "NUMBER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "LPAREN", "RPAREN", "PLUS", "MINUS", "MUL", "DIV", 
                      "GT", "LT", "EQ", "GTEQ", "LTEQ", "NEQ", "AND", "OR", 
                      "IF", "THEN", "ELSE", "ENDIF", "WHILE", "ENDWHILE", 
                      "ID", "WS", "COMMENT", "NEWLINE", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declarationStatement = 2
    RULE_whileStatement = 3
    RULE_ifStatement = 4
    RULE_expression = 5
    RULE_logicalExpression = 6
    RULE_booleanExpression = 7
    RULE_atomBoolean = 8
    RULE_arithmeticalExpression = 9
    RULE_additiveExpression = 10
    RULE_multiplicativeExpression = 11
    RULE_atomNumber = 12
    RULE_stringExpression = 13
    RULE_additiveStringExpression = 14
    RULE_atomString = 15
    RULE_literal = 16
    RULE_signedNumber = 17
    RULE_string = 18
    RULE_boolean = 19
    RULE_id = 20

    ruleNames =  [ "program", "statement", "declarationStatement", "whileStatement", 
                   "ifStatement", "expression", "logicalExpression", "booleanExpression", 
                   "atomBoolean", "arithmeticalExpression", "additiveExpression", 
                   "multiplicativeExpression", "atomNumber", "stringExpression", 
                   "additiveStringExpression", "atomString", "literal", 
                   "signedNumber", "string", "boolean", "id" ]

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
    IF=18
    THEN=19
    ELSE=20
    ENDIF=21
    WHILE=22
    ENDWHILE=23
    ID=24
    WS=25
    COMMENT=26
    NEWLINE=27
    LINE_COMMENT=28

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
            self.state = 43 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self.statement()
                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 21233664) != 0)):
                    break

            self.state = 47
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


        def whileStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.WhileStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.IfStatementContext,0)


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
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.declarationStatement()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.whileStatement()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.ifStatement()
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
            self.state = 54
            self.match(SmallerBasicParser.ID)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 55
                self.match(SmallerBasicParser.EQ)
                self.state = 56
                self.expression()


            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 59
                self.match(SmallerBasicParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(SmallerBasicParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(SmallerBasicParser.LPAREN, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.LogicalExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SmallerBasicParser.RPAREN, 0)

        def ENDWHILE(self):
            return self.getToken(SmallerBasicParser.ENDWHILE, 0)

        def NEWLINE(self):
            return self.getToken(SmallerBasicParser.NEWLINE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.StatementContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.StatementContext,i)


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = SmallerBasicParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(SmallerBasicParser.WHILE)
            self.state = 63
            self.match(SmallerBasicParser.LPAREN)
            self.state = 64
            self.logicalExpression()
            self.state = 65
            self.match(SmallerBasicParser.RPAREN)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 66
                self.match(SmallerBasicParser.NEWLINE)


            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.statement()
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 21233664) != 0)):
                    break

            self.state = 74
            self.match(SmallerBasicParser.ENDWHILE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SmallerBasicParser.IF, 0)

        def LPAREN(self):
            return self.getToken(SmallerBasicParser.LPAREN, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.LogicalExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SmallerBasicParser.RPAREN, 0)

        def THEN(self):
            return self.getToken(SmallerBasicParser.THEN, 0)

        def ENDIF(self):
            return self.getToken(SmallerBasicParser.ENDIF, 0)

        def NEWLINE(self):
            return self.getToken(SmallerBasicParser.NEWLINE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.StatementContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.StatementContext,i)


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = SmallerBasicParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(SmallerBasicParser.IF)
            self.state = 77
            self.match(SmallerBasicParser.LPAREN)
            self.state = 78
            self.logicalExpression()
            self.state = 79
            self.match(SmallerBasicParser.RPAREN)
            self.state = 80
            self.match(SmallerBasicParser.THEN)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 81
                self.match(SmallerBasicParser.NEWLINE)


            self.state = 85 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 84
                self.statement()
                self.state = 87 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 21233664) != 0)):
                    break

            self.state = 89
            self.match(SmallerBasicParser.ENDIF)
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
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.arithmeticalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.logicalExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.stringExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 94
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
        self.enterRule(localctx, 12, self.RULE_logicalExpression)
        self._la = 0 # Token type
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.booleanExpression()
                self.state = 100 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 98
                    _la = self._input.LA(1)
                    if not(_la==16 or _la==17):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 99
                    self.booleanExpression()
                    self.state = 102 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==16 or _la==17):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
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
        self.enterRule(localctx, 14, self.RULE_booleanExpression)
        self._la = 0 # Token type
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.arithmeticalExpression()
                self.state = 108
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64512) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 109
                self.arithmeticalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
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
        self.enterRule(localctx, 16, self.RULE_atomBoolean)
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.boolean()
                pass
            elif token in [6, 7, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.id_()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                self.match(SmallerBasicParser.LPAREN)
                self.state = 117
                self.logicalExpression()
                self.state = 118
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
        self.enterRule(localctx, 18, self.RULE_arithmeticalExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
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
        self.enterRule(localctx, 20, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.multiplicativeExpression()
                self.state = 127 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 125
                    _la = self._input.LA(1)
                    if not(_la==6 or _la==7):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 126
                    self.multiplicativeExpression()
                    self.state = 129 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==6 or _la==7):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
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
        self.enterRule(localctx, 22, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.atomNumber()
                self.state = 137 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 135
                    _la = self._input.LA(1)
                    if not(_la==8 or _la==9):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 136
                    self.atomNumber()
                    self.state = 139 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==8 or _la==9):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
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
        self.enterRule(localctx, 24, self.RULE_atomNumber)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.signedNumber()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.id_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.match(SmallerBasicParser.LPAREN)
                self.state = 147
                self.arithmeticalExpression()
                self.state = 148
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
        self.enterRule(localctx, 26, self.RULE_stringExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
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
        self.enterRule(localctx, 28, self.RULE_additiveStringExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.atomString()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 155
                self.match(SmallerBasicParser.PLUS)
                self.state = 156
                self.atomString()
                self.state = 161
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
        self.enterRule(localctx, 30, self.RULE_atomString)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.string()
                pass
            elif token in [6, 7, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
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
        self.enterRule(localctx, 32, self.RULE_literal)
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.signedNumber()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.string()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                self.boolean()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 169
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
        self.enterRule(localctx, 34, self.RULE_signedNumber)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==7:
                self.state = 172
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 175
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
        self.enterRule(localctx, 36, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
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
        self.enterRule(localctx, 38, self.RULE_boolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
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
        self.enterRule(localctx, 40, self.RULE_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==7:
                self.state = 181
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 184
            self.match(SmallerBasicParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





