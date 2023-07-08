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
        4,1,36,258,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,4,0,50,8,0,11,0,12,0,51,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,4,2,72,8,2,11,2,12,2,73,1,2,1,2,1,2,3,2,79,8,2,1,3,1,3,1,
        3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,4,5,93,8,5,11,5,12,5,94,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,4,5,105,8,5,11,5,12,5,106,1,5,1,5,
        4,5,111,8,5,11,5,12,5,112,1,5,1,5,3,5,117,8,5,1,6,1,6,1,6,1,6,1,
        6,4,6,124,8,6,11,6,12,6,125,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        4,7,137,8,7,11,7,12,7,138,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,4,7,152,8,7,11,7,12,7,153,1,7,1,7,3,7,158,8,7,1,8,1,8,1,8,
        1,8,3,8,164,8,8,1,9,1,9,1,9,4,9,169,8,9,11,9,12,9,170,1,9,3,9,174,
        8,9,1,10,1,10,1,10,1,10,1,10,3,10,181,8,10,1,11,1,11,1,11,1,11,1,
        11,1,11,3,11,189,8,11,1,12,1,12,1,13,1,13,1,13,4,13,196,8,13,11,
        13,12,13,197,1,13,3,13,201,8,13,1,14,1,14,1,14,4,14,206,8,14,11,
        14,12,14,207,1,14,3,14,211,8,14,1,15,1,15,1,15,3,15,216,8,15,1,15,
        1,15,1,15,1,15,3,15,222,8,15,1,16,1,16,1,17,1,17,1,17,5,17,229,8,
        17,10,17,12,17,232,9,17,1,18,1,18,3,18,236,8,18,1,19,1,19,1,19,1,
        19,3,19,242,8,19,1,20,3,20,245,8,20,1,20,1,20,1,21,1,21,1,22,1,22,
        1,23,3,23,254,8,23,1,23,1,23,1,23,0,0,24,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,4,1,0,19,20,1,0,13,18,
        1,0,9,10,1,0,11,12,271,0,49,1,0,0,0,2,61,1,0,0,0,4,78,1,0,0,0,6,
        80,1,0,0,0,8,83,1,0,0,0,10,116,1,0,0,0,12,118,1,0,0,0,14,157,1,0,
        0,0,16,163,1,0,0,0,18,173,1,0,0,0,20,180,1,0,0,0,22,188,1,0,0,0,
        24,190,1,0,0,0,26,200,1,0,0,0,28,210,1,0,0,0,30,221,1,0,0,0,32,223,
        1,0,0,0,34,225,1,0,0,0,36,235,1,0,0,0,38,241,1,0,0,0,40,244,1,0,
        0,0,42,248,1,0,0,0,44,250,1,0,0,0,46,253,1,0,0,0,48,50,3,2,1,0,49,
        48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,
        0,53,54,5,0,0,1,54,1,1,0,0,0,55,62,3,4,2,0,56,62,3,12,6,0,57,62,
        3,14,7,0,58,62,3,10,5,0,59,62,3,6,3,0,60,62,3,8,4,0,61,55,1,0,0,
        0,61,56,1,0,0,0,61,57,1,0,0,0,61,58,1,0,0,0,61,59,1,0,0,0,61,60,
        1,0,0,0,62,3,1,0,0,0,63,64,5,32,0,0,64,65,5,15,0,0,65,79,3,16,8,
        0,66,71,5,32,0,0,67,68,5,6,0,0,68,69,3,24,12,0,69,70,5,7,0,0,70,
        72,1,0,0,0,71,67,1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,
        0,74,75,1,0,0,0,75,76,5,15,0,0,76,77,3,16,8,0,77,79,1,0,0,0,78,63,
        1,0,0,0,78,66,1,0,0,0,79,5,1,0,0,0,80,81,5,32,0,0,81,82,5,8,0,0,
        82,7,1,0,0,0,83,84,5,31,0,0,84,85,5,32,0,0,85,9,1,0,0,0,86,87,5,
        21,0,0,87,88,5,4,0,0,88,89,3,18,9,0,89,90,5,5,0,0,90,92,5,22,0,0,
        91,93,3,2,1,0,92,91,1,0,0,0,93,94,1,0,0,0,94,92,1,0,0,0,94,95,1,
        0,0,0,95,96,1,0,0,0,96,97,5,24,0,0,97,117,1,0,0,0,98,99,5,21,0,0,
        99,100,5,4,0,0,100,101,3,18,9,0,101,102,5,5,0,0,102,104,5,22,0,0,
        103,105,3,2,1,0,104,103,1,0,0,0,105,106,1,0,0,0,106,104,1,0,0,0,
        106,107,1,0,0,0,107,108,1,0,0,0,108,110,5,23,0,0,109,111,3,2,1,0,
        110,109,1,0,0,0,111,112,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,
        113,114,1,0,0,0,114,115,5,24,0,0,115,117,1,0,0,0,116,86,1,0,0,0,
        116,98,1,0,0,0,117,11,1,0,0,0,118,119,5,25,0,0,119,120,5,4,0,0,120,
        121,3,18,9,0,121,123,5,5,0,0,122,124,3,2,1,0,123,122,1,0,0,0,124,
        125,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,127,1,0,0,0,127,
        128,5,26,0,0,128,13,1,0,0,0,129,130,5,27,0,0,130,131,5,32,0,0,131,
        132,5,15,0,0,132,133,3,24,12,0,133,134,5,28,0,0,134,136,3,24,12,
        0,135,137,3,2,1,0,136,135,1,0,0,0,137,138,1,0,0,0,138,136,1,0,0,
        0,138,139,1,0,0,0,139,140,1,0,0,0,140,141,5,30,0,0,141,158,1,0,0,
        0,142,143,5,27,0,0,143,144,5,32,0,0,144,145,5,15,0,0,145,146,3,24,
        12,0,146,147,5,28,0,0,147,148,3,24,12,0,148,149,5,29,0,0,149,151,
        3,24,12,0,150,152,3,2,1,0,151,150,1,0,0,0,152,153,1,0,0,0,153,151,
        1,0,0,0,153,154,1,0,0,0,154,155,1,0,0,0,155,156,5,30,0,0,156,158,
        1,0,0,0,157,129,1,0,0,0,157,142,1,0,0,0,158,15,1,0,0,0,159,164,3,
        24,12,0,160,164,3,18,9,0,161,164,3,32,16,0,162,164,3,38,19,0,163,
        159,1,0,0,0,163,160,1,0,0,0,163,161,1,0,0,0,163,162,1,0,0,0,164,
        17,1,0,0,0,165,168,3,20,10,0,166,167,7,0,0,0,167,169,3,20,10,0,168,
        166,1,0,0,0,169,170,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,
        174,1,0,0,0,172,174,3,20,10,0,173,165,1,0,0,0,173,172,1,0,0,0,174,
        19,1,0,0,0,175,176,3,24,12,0,176,177,7,1,0,0,177,178,3,24,12,0,178,
        181,1,0,0,0,179,181,3,22,11,0,180,175,1,0,0,0,180,179,1,0,0,0,181,
        21,1,0,0,0,182,189,3,44,22,0,183,189,3,46,23,0,184,185,5,4,0,0,185,
        186,3,18,9,0,186,187,5,5,0,0,187,189,1,0,0,0,188,182,1,0,0,0,188,
        183,1,0,0,0,188,184,1,0,0,0,189,23,1,0,0,0,190,191,3,26,13,0,191,
        25,1,0,0,0,192,195,3,28,14,0,193,194,7,2,0,0,194,196,3,28,14,0,195,
        193,1,0,0,0,196,197,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,
        201,1,0,0,0,199,201,3,28,14,0,200,192,1,0,0,0,200,199,1,0,0,0,201,
        27,1,0,0,0,202,205,3,30,15,0,203,204,7,3,0,0,204,206,3,30,15,0,205,
        203,1,0,0,0,206,207,1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,
        211,1,0,0,0,209,211,3,30,15,0,210,202,1,0,0,0,210,209,1,0,0,0,211,
        29,1,0,0,0,212,222,3,40,20,0,213,222,3,46,23,0,214,216,5,10,0,0,
        215,214,1,0,0,0,215,216,1,0,0,0,216,217,1,0,0,0,217,218,5,4,0,0,
        218,219,3,24,12,0,219,220,5,5,0,0,220,222,1,0,0,0,221,212,1,0,0,
        0,221,213,1,0,0,0,221,215,1,0,0,0,222,31,1,0,0,0,223,224,3,34,17,
        0,224,33,1,0,0,0,225,230,3,36,18,0,226,227,5,9,0,0,227,229,3,36,
        18,0,228,226,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,
        0,0,231,35,1,0,0,0,232,230,1,0,0,0,233,236,3,42,21,0,234,236,3,46,
        23,0,235,233,1,0,0,0,235,234,1,0,0,0,236,37,1,0,0,0,237,242,3,40,
        20,0,238,242,3,42,21,0,239,242,3,44,22,0,240,242,3,46,23,0,241,237,
        1,0,0,0,241,238,1,0,0,0,241,239,1,0,0,0,241,240,1,0,0,0,242,39,1,
        0,0,0,243,245,7,2,0,0,244,243,1,0,0,0,244,245,1,0,0,0,245,246,1,
        0,0,0,246,247,5,1,0,0,247,41,1,0,0,0,248,249,5,2,0,0,249,43,1,0,
        0,0,250,251,5,3,0,0,251,45,1,0,0,0,252,254,7,2,0,0,253,252,1,0,0,
        0,253,254,1,0,0,0,254,255,1,0,0,0,255,256,5,32,0,0,256,47,1,0,0,
        0,28,51,61,73,78,94,106,112,116,125,138,153,157,163,170,173,180,
        188,197,200,207,210,215,221,230,235,241,244,253
    ]

class SmallerBasicParser ( Parser ):

    grammarFileName = "SmallerBasic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "':'", "'+'", "'-'", "'*'", 
                     "'/'", "'>'", "'<'", "'='", "'>='", "'<='", "'<>'", 
                     "'And'", "'Or'", "'If'", "'Then'", "'Else'", "'EndIf'", 
                     "'While'", "'EndWhile'", "'For'", "'To'", "'Step'", 
                     "'EndFor'", "'Goto'" ]

    symbolicNames = [ "<INVALID>", "NUMBER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "LROUND", "RROUND", "LSQUARE", "RSQUARE", "COLON", 
                      "PLUS", "MINUS", "MUL", "DIV", "GT", "LT", "EQ", "GTEQ", 
                      "LTEQ", "NEQ", "AND", "OR", "IF", "THEN", "ELSE", 
                      "ENDIF", "WHILE", "ENDWHILE", "FOR", "TO", "STEP", 
                      "ENDFOR", "GOTO", "ID", "WS", "COMMENT", "NEWLINE", 
                      "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declarationStatement = 2
    RULE_labelStatement = 3
    RULE_gotoStatement = 4
    RULE_ifStatement = 5
    RULE_whileStatement = 6
    RULE_forStatement = 7
    RULE_expression = 8
    RULE_logicalExpression = 9
    RULE_booleanExpression = 10
    RULE_atomBoolean = 11
    RULE_arithmeticalExpression = 12
    RULE_additiveExpression = 13
    RULE_multiplicativeExpression = 14
    RULE_atomNumber = 15
    RULE_stringExpression = 16
    RULE_additiveStringExpression = 17
    RULE_atomString = 18
    RULE_literal = 19
    RULE_signedNumber = 20
    RULE_string = 21
    RULE_boolean = 22
    RULE_id = 23

    ruleNames =  [ "program", "statement", "declarationStatement", "labelStatement", 
                   "gotoStatement", "ifStatement", "whileStatement", "forStatement", 
                   "expression", "logicalExpression", "booleanExpression", 
                   "atomBoolean", "arithmeticalExpression", "additiveExpression", 
                   "multiplicativeExpression", "atomNumber", "stringExpression", 
                   "additiveStringExpression", "atomString", "literal", 
                   "signedNumber", "string", "boolean", "id" ]

    EOF = Token.EOF
    NUMBER_LITERAL=1
    STRING_LITERAL=2
    BOOLEAN_LITERAL=3
    LROUND=4
    RROUND=5
    LSQUARE=6
    RSQUARE=7
    COLON=8
    PLUS=9
    MINUS=10
    MUL=11
    DIV=12
    GT=13
    LT=14
    EQ=15
    GTEQ=16
    LTEQ=17
    NEQ=18
    AND=19
    OR=20
    IF=21
    THEN=22
    ELSE=23
    ENDIF=24
    WHILE=25
    ENDWHILE=26
    FOR=27
    TO=28
    STEP=29
    ENDFOR=30
    GOTO=31
    ID=32
    WS=33
    COMMENT=34
    NEWLINE=35
    LINE_COMMENT=36

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
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.statement()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6612320256) != 0)):
                    break

            self.state = 53
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


        def forStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.ForStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.IfStatementContext,0)


        def labelStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.LabelStatementContext,0)


        def gotoStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.GotoStatementContext,0)


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
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.declarationStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.whileStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.forStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.labelStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 60
                self.gotoStatement()
                pass


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


        def LSQUARE(self, i:int=None):
            if i is None:
                return self.getTokens(SmallerBasicParser.LSQUARE)
            else:
                return self.getToken(SmallerBasicParser.LSQUARE, i)

        def arithmeticalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.ArithmeticalExpressionContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.ArithmeticalExpressionContext,i)


        def RSQUARE(self, i:int=None):
            if i is None:
                return self.getTokens(SmallerBasicParser.RSQUARE)
            else:
                return self.getToken(SmallerBasicParser.RSQUARE, i)

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
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(SmallerBasicParser.ID)
                self.state = 64
                self.match(SmallerBasicParser.EQ)
                self.state = 65
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(SmallerBasicParser.ID)
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 67
                    self.match(SmallerBasicParser.LSQUARE)
                    self.state = 68
                    self.arithmeticalExpression()
                    self.state = 69
                    self.match(SmallerBasicParser.RSQUARE)
                    self.state = 73 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==6):
                        break

                self.state = 75
                self.match(SmallerBasicParser.EQ)
                self.state = 76
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)

        def COLON(self):
            return self.getToken(SmallerBasicParser.COLON, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_labelStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelStatement" ):
                listener.enterLabelStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelStatement" ):
                listener.exitLabelStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelStatement" ):
                return visitor.visitLabelStatement(self)
            else:
                return visitor.visitChildren(self)




    def labelStatement(self):

        localctx = SmallerBasicParser.LabelStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_labelStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(SmallerBasicParser.ID)
            self.state = 81
            self.match(SmallerBasicParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOTO(self):
            return self.getToken(SmallerBasicParser.GOTO, 0)

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_gotoStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGotoStatement" ):
                listener.enterGotoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGotoStatement" ):
                listener.exitGotoStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGotoStatement" ):
                return visitor.visitGotoStatement(self)
            else:
                return visitor.visitChildren(self)




    def gotoStatement(self):

        localctx = SmallerBasicParser.GotoStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_gotoStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(SmallerBasicParser.GOTO)
            self.state = 84
            self.match(SmallerBasicParser.ID)
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

        def LROUND(self):
            return self.getToken(SmallerBasicParser.LROUND, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.LogicalExpressionContext,0)


        def RROUND(self):
            return self.getToken(SmallerBasicParser.RROUND, 0)

        def THEN(self):
            return self.getToken(SmallerBasicParser.THEN, 0)

        def ENDIF(self):
            return self.getToken(SmallerBasicParser.ENDIF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.StatementContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(SmallerBasicParser.ELSE, 0)

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
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(SmallerBasicParser.IF)
                self.state = 87
                self.match(SmallerBasicParser.LROUND)
                self.state = 88
                self.logicalExpression()
                self.state = 89
                self.match(SmallerBasicParser.RROUND)
                self.state = 90
                self.match(SmallerBasicParser.THEN)
                self.state = 92 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 91
                    self.statement()
                    self.state = 94 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6612320256) != 0)):
                        break

                self.state = 96
                self.match(SmallerBasicParser.ENDIF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(SmallerBasicParser.IF)
                self.state = 99
                self.match(SmallerBasicParser.LROUND)
                self.state = 100
                self.logicalExpression()
                self.state = 101
                self.match(SmallerBasicParser.RROUND)
                self.state = 102
                self.match(SmallerBasicParser.THEN)
                self.state = 104 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 103
                    self.statement()
                    self.state = 106 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6612320256) != 0)):
                        break

                self.state = 108
                self.match(SmallerBasicParser.ELSE)
                self.state = 110 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 109
                    self.statement()
                    self.state = 112 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6612320256) != 0)):
                        break

                self.state = 114
                self.match(SmallerBasicParser.ENDIF)
                pass


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

        def LROUND(self):
            return self.getToken(SmallerBasicParser.LROUND, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.LogicalExpressionContext,0)


        def RROUND(self):
            return self.getToken(SmallerBasicParser.RROUND, 0)

        def ENDWHILE(self):
            return self.getToken(SmallerBasicParser.ENDWHILE, 0)

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
        self.enterRule(localctx, 12, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(SmallerBasicParser.WHILE)
            self.state = 119
            self.match(SmallerBasicParser.LROUND)
            self.state = 120
            self.logicalExpression()
            self.state = 121
            self.match(SmallerBasicParser.RROUND)
            self.state = 123 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 122
                self.statement()
                self.state = 125 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6612320256) != 0)):
                    break

            self.state = 127
            self.match(SmallerBasicParser.ENDWHILE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(SmallerBasicParser.FOR, 0)

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)

        def EQ(self):
            return self.getToken(SmallerBasicParser.EQ, 0)

        def arithmeticalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.ArithmeticalExpressionContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.ArithmeticalExpressionContext,i)


        def TO(self):
            return self.getToken(SmallerBasicParser.TO, 0)

        def ENDFOR(self):
            return self.getToken(SmallerBasicParser.ENDFOR, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.StatementContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.StatementContext,i)


        def STEP(self):
            return self.getToken(SmallerBasicParser.STEP, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = SmallerBasicParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(SmallerBasicParser.FOR)
                self.state = 130
                self.match(SmallerBasicParser.ID)
                self.state = 131
                self.match(SmallerBasicParser.EQ)
                self.state = 132
                self.arithmeticalExpression()
                self.state = 133
                self.match(SmallerBasicParser.TO)
                self.state = 134
                self.arithmeticalExpression()
                self.state = 136 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 135
                    self.statement()
                    self.state = 138 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6612320256) != 0)):
                        break

                self.state = 140
                self.match(SmallerBasicParser.ENDFOR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(SmallerBasicParser.FOR)
                self.state = 143
                self.match(SmallerBasicParser.ID)
                self.state = 144
                self.match(SmallerBasicParser.EQ)
                self.state = 145
                self.arithmeticalExpression()
                self.state = 146
                self.match(SmallerBasicParser.TO)
                self.state = 147
                self.arithmeticalExpression()
                self.state = 148
                self.match(SmallerBasicParser.STEP)
                self.state = 149
                self.arithmeticalExpression()
                self.state = 151 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 150
                    self.statement()
                    self.state = 153 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6612320256) != 0)):
                        break

                self.state = 155
                self.match(SmallerBasicParser.ENDFOR)
                pass


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
        self.enterRule(localctx, 16, self.RULE_expression)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.arithmeticalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.logicalExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.stringExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
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
        self.enterRule(localctx, 18, self.RULE_logicalExpression)
        self._la = 0 # Token type
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.booleanExpression()
                self.state = 168 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 166
                    _la = self._input.LA(1)
                    if not(_la==19 or _la==20):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 167
                    self.booleanExpression()
                    self.state = 170 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==19 or _la==20):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
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
        self.enterRule(localctx, 20, self.RULE_booleanExpression)
        self._la = 0 # Token type
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.arithmeticalExpression()
                self.state = 176
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 177
                self.arithmeticalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
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


        def LROUND(self):
            return self.getToken(SmallerBasicParser.LROUND, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.LogicalExpressionContext,0)


        def RROUND(self):
            return self.getToken(SmallerBasicParser.RROUND, 0)

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
        self.enterRule(localctx, 22, self.RULE_atomBoolean)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.boolean()
                pass
            elif token in [9, 10, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.id_()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.match(SmallerBasicParser.LROUND)
                self.state = 185
                self.logicalExpression()
                self.state = 186
                self.match(SmallerBasicParser.RROUND)
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
        self.enterRule(localctx, 24, self.RULE_arithmeticalExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
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
        self.enterRule(localctx, 26, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.multiplicativeExpression()
                self.state = 195 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 193
                    _la = self._input.LA(1)
                    if not(_la==9 or _la==10):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 194
                    self.multiplicativeExpression()
                    self.state = 197 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==9 or _la==10):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
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
        self.enterRule(localctx, 28, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.atomNumber()
                self.state = 205 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 203
                    _la = self._input.LA(1)
                    if not(_la==11 or _la==12):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 204
                    self.atomNumber()
                    self.state = 207 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==11 or _la==12):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
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


        def LROUND(self):
            return self.getToken(SmallerBasicParser.LROUND, 0)

        def arithmeticalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.ArithmeticalExpressionContext,0)


        def RROUND(self):
            return self.getToken(SmallerBasicParser.RROUND, 0)

        def MINUS(self):
            return self.getToken(SmallerBasicParser.MINUS, 0)

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
        self.enterRule(localctx, 30, self.RULE_atomNumber)
        self._la = 0 # Token type
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.signedNumber()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.id_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 214
                    self.match(SmallerBasicParser.MINUS)


                self.state = 217
                self.match(SmallerBasicParser.LROUND)
                self.state = 218
                self.arithmeticalExpression()
                self.state = 219
                self.match(SmallerBasicParser.RROUND)
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
        self.enterRule(localctx, 32, self.RULE_stringExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
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
        self.enterRule(localctx, 34, self.RULE_additiveStringExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.atomString()
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 226
                self.match(SmallerBasicParser.PLUS)
                self.state = 227
                self.atomString()
                self.state = 232
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
        self.enterRule(localctx, 36, self.RULE_atomString)
        try:
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.string()
                pass
            elif token in [9, 10, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
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
        self.enterRule(localctx, 38, self.RULE_literal)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.signedNumber()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.string()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.boolean()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 240
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
        self.enterRule(localctx, 40, self.RULE_signedNumber)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9 or _la==10:
                self.state = 243
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 246
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
        self.enterRule(localctx, 42, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
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
        self.enterRule(localctx, 44, self.RULE_boolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
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
        self.enterRule(localctx, 46, self.RULE_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9 or _la==10:
                self.state = 252
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 255
            self.match(SmallerBasicParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





