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
        4,1,40,308,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,4,0,58,8,0,11,0,12,0,59,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,73,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,
        83,8,2,11,2,12,2,84,1,2,1,2,1,2,3,2,90,8,2,1,3,1,3,1,3,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,1,5,4,5,104,8,5,11,5,12,5,105,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,4,5,116,8,5,11,5,12,5,117,1,5,1,5,4,5,122,8,
        5,11,5,12,5,123,1,5,1,5,3,5,128,8,5,1,6,1,6,1,6,1,6,1,6,4,6,135,
        8,6,11,6,12,6,136,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,4,7,148,8,
        7,11,7,12,7,149,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,4,7,
        163,8,7,11,7,12,7,164,1,7,1,7,3,7,169,8,7,1,8,1,8,1,8,4,8,174,8,
        8,11,8,12,8,175,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,4,10,187,
        8,10,11,10,12,10,188,1,10,1,10,3,10,193,8,10,1,10,1,10,1,11,1,11,
        1,11,1,11,3,11,201,8,11,1,12,1,12,1,12,4,12,206,8,12,11,12,12,12,
        207,1,12,3,12,211,8,12,1,13,1,13,1,13,1,13,1,13,3,13,218,8,13,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,227,8,14,1,15,1,15,1,16,1,
        16,1,16,4,16,234,8,16,11,16,12,16,235,1,16,3,16,239,8,16,1,17,1,
        17,1,17,4,17,244,8,17,11,17,12,17,245,1,17,3,17,249,8,17,1,18,1,
        18,1,18,1,18,3,18,255,8,18,1,18,1,18,1,18,1,18,1,18,3,18,262,8,18,
        1,18,3,18,265,8,18,1,19,1,19,1,20,1,20,1,20,5,20,272,8,20,10,20,
        12,20,275,9,20,1,21,1,21,1,21,3,21,280,8,21,1,22,1,22,1,22,1,22,
        1,22,3,22,287,8,22,1,23,3,23,290,8,23,1,23,1,23,1,24,3,24,295,8,
        24,1,24,1,24,1,25,1,25,1,26,1,26,1,27,3,27,304,8,27,1,27,1,27,1,
        27,0,0,28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,0,4,1,0,19,20,1,0,13,18,1,0,9,10,1,0,11,
        12,330,0,57,1,0,0,0,2,72,1,0,0,0,4,89,1,0,0,0,6,91,1,0,0,0,8,94,
        1,0,0,0,10,127,1,0,0,0,12,129,1,0,0,0,14,168,1,0,0,0,16,170,1,0,
        0,0,18,179,1,0,0,0,20,183,1,0,0,0,22,200,1,0,0,0,24,210,1,0,0,0,
        26,217,1,0,0,0,28,226,1,0,0,0,30,228,1,0,0,0,32,238,1,0,0,0,34,248,
        1,0,0,0,36,264,1,0,0,0,38,266,1,0,0,0,40,268,1,0,0,0,42,279,1,0,
        0,0,44,286,1,0,0,0,46,289,1,0,0,0,48,294,1,0,0,0,50,298,1,0,0,0,
        52,300,1,0,0,0,54,303,1,0,0,0,56,58,3,2,1,0,57,56,1,0,0,0,58,59,
        1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,62,5,0,0,1,
        62,1,1,0,0,0,63,73,3,4,2,0,64,73,3,12,6,0,65,73,3,14,7,0,66,73,3,
        10,5,0,67,73,3,6,3,0,68,73,3,8,4,0,69,73,3,16,8,0,70,73,3,18,9,0,
        71,73,3,20,10,0,72,63,1,0,0,0,72,64,1,0,0,0,72,65,1,0,0,0,72,66,
        1,0,0,0,72,67,1,0,0,0,72,68,1,0,0,0,72,69,1,0,0,0,72,70,1,0,0,0,
        72,71,1,0,0,0,73,3,1,0,0,0,74,75,5,34,0,0,75,76,5,15,0,0,76,90,3,
        22,11,0,77,82,5,34,0,0,78,79,5,5,0,0,79,80,3,30,15,0,80,81,5,6,0,
        0,81,83,1,0,0,0,82,78,1,0,0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,85,
        1,0,0,0,85,86,1,0,0,0,86,87,5,15,0,0,87,88,3,22,11,0,88,90,1,0,0,
        0,89,74,1,0,0,0,89,77,1,0,0,0,90,5,1,0,0,0,91,92,5,34,0,0,92,93,
        5,8,0,0,93,7,1,0,0,0,94,95,5,31,0,0,95,96,5,34,0,0,96,9,1,0,0,0,
        97,98,5,21,0,0,98,99,5,3,0,0,99,100,3,24,12,0,100,101,5,4,0,0,101,
        103,5,22,0,0,102,104,3,2,1,0,103,102,1,0,0,0,104,105,1,0,0,0,105,
        103,1,0,0,0,105,106,1,0,0,0,106,107,1,0,0,0,107,108,5,24,0,0,108,
        128,1,0,0,0,109,110,5,21,0,0,110,111,5,3,0,0,111,112,3,24,12,0,112,
        113,5,4,0,0,113,115,5,22,0,0,114,116,3,2,1,0,115,114,1,0,0,0,116,
        117,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,
        121,5,23,0,0,120,122,3,2,1,0,121,120,1,0,0,0,122,123,1,0,0,0,123,
        121,1,0,0,0,123,124,1,0,0,0,124,125,1,0,0,0,125,126,5,24,0,0,126,
        128,1,0,0,0,127,97,1,0,0,0,127,109,1,0,0,0,128,11,1,0,0,0,129,130,
        5,25,0,0,130,131,5,3,0,0,131,132,3,24,12,0,132,134,5,4,0,0,133,135,
        3,2,1,0,134,133,1,0,0,0,135,136,1,0,0,0,136,134,1,0,0,0,136,137,
        1,0,0,0,137,138,1,0,0,0,138,139,5,26,0,0,139,13,1,0,0,0,140,141,
        5,27,0,0,141,142,5,34,0,0,142,143,5,15,0,0,143,144,3,30,15,0,144,
        145,5,28,0,0,145,147,3,30,15,0,146,148,3,2,1,0,147,146,1,0,0,0,148,
        149,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,
        152,5,30,0,0,152,169,1,0,0,0,153,154,5,27,0,0,154,155,5,34,0,0,155,
        156,5,15,0,0,156,157,3,30,15,0,157,158,5,28,0,0,158,159,3,30,15,
        0,159,160,5,29,0,0,160,162,3,30,15,0,161,163,3,2,1,0,162,161,1,0,
        0,0,163,164,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,166,1,0,
        0,0,166,167,5,30,0,0,167,169,1,0,0,0,168,140,1,0,0,0,168,153,1,0,
        0,0,169,15,1,0,0,0,170,171,5,32,0,0,171,173,5,34,0,0,172,174,3,2,
        1,0,173,172,1,0,0,0,174,175,1,0,0,0,175,173,1,0,0,0,175,176,1,0,
        0,0,176,177,1,0,0,0,177,178,5,33,0,0,178,17,1,0,0,0,179,180,5,34,
        0,0,180,181,5,3,0,0,181,182,5,4,0,0,182,19,1,0,0,0,183,186,5,34,
        0,0,184,185,5,7,0,0,185,187,5,34,0,0,186,184,1,0,0,0,187,188,1,0,
        0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,190,192,5,3,
        0,0,191,193,3,22,11,0,192,191,1,0,0,0,192,193,1,0,0,0,193,194,1,
        0,0,0,194,195,5,4,0,0,195,21,1,0,0,0,196,201,3,44,22,0,197,201,3,
        24,12,0,198,201,3,30,15,0,199,201,3,38,19,0,200,196,1,0,0,0,200,
        197,1,0,0,0,200,198,1,0,0,0,200,199,1,0,0,0,201,23,1,0,0,0,202,205,
        3,26,13,0,203,204,7,0,0,0,204,206,3,26,13,0,205,203,1,0,0,0,206,
        207,1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,211,1,0,0,0,209,
        211,3,26,13,0,210,202,1,0,0,0,210,209,1,0,0,0,211,25,1,0,0,0,212,
        213,3,30,15,0,213,214,7,1,0,0,214,215,3,30,15,0,215,218,1,0,0,0,
        216,218,3,28,14,0,217,212,1,0,0,0,217,216,1,0,0,0,218,27,1,0,0,0,
        219,227,3,52,26,0,220,221,5,3,0,0,221,222,3,24,12,0,222,223,5,4,
        0,0,223,227,1,0,0,0,224,227,3,20,10,0,225,227,5,34,0,0,226,219,1,
        0,0,0,226,220,1,0,0,0,226,224,1,0,0,0,226,225,1,0,0,0,227,29,1,0,
        0,0,228,229,3,32,16,0,229,31,1,0,0,0,230,233,3,34,17,0,231,232,7,
        2,0,0,232,234,3,34,17,0,233,231,1,0,0,0,234,235,1,0,0,0,235,233,
        1,0,0,0,235,236,1,0,0,0,236,239,1,0,0,0,237,239,3,34,17,0,238,230,
        1,0,0,0,238,237,1,0,0,0,239,33,1,0,0,0,240,243,3,36,18,0,241,242,
        7,3,0,0,242,244,3,34,17,0,243,241,1,0,0,0,244,245,1,0,0,0,245,243,
        1,0,0,0,245,246,1,0,0,0,246,249,1,0,0,0,247,249,3,36,18,0,248,240,
        1,0,0,0,248,247,1,0,0,0,249,35,1,0,0,0,250,265,3,46,23,0,251,265,
        3,48,24,0,252,265,3,54,27,0,253,255,5,10,0,0,254,253,1,0,0,0,254,
        255,1,0,0,0,255,256,1,0,0,0,256,257,5,3,0,0,257,258,3,30,15,0,258,
        259,5,4,0,0,259,265,1,0,0,0,260,262,5,10,0,0,261,260,1,0,0,0,261,
        262,1,0,0,0,262,263,1,0,0,0,263,265,3,20,10,0,264,250,1,0,0,0,264,
        251,1,0,0,0,264,252,1,0,0,0,264,254,1,0,0,0,264,261,1,0,0,0,265,
        37,1,0,0,0,266,267,3,40,20,0,267,39,1,0,0,0,268,273,3,42,21,0,269,
        270,5,9,0,0,270,272,3,40,20,0,271,269,1,0,0,0,272,275,1,0,0,0,273,
        271,1,0,0,0,273,274,1,0,0,0,274,41,1,0,0,0,275,273,1,0,0,0,276,280,
        3,50,25,0,277,280,5,34,0,0,278,280,3,20,10,0,279,276,1,0,0,0,279,
        277,1,0,0,0,279,278,1,0,0,0,280,43,1,0,0,0,281,287,3,46,23,0,282,
        287,3,48,24,0,283,287,3,50,25,0,284,287,3,52,26,0,285,287,3,54,27,
        0,286,281,1,0,0,0,286,282,1,0,0,0,286,283,1,0,0,0,286,284,1,0,0,
        0,286,285,1,0,0,0,287,45,1,0,0,0,288,290,7,2,0,0,289,288,1,0,0,0,
        289,290,1,0,0,0,290,291,1,0,0,0,291,292,5,35,0,0,292,47,1,0,0,0,
        293,295,7,2,0,0,294,293,1,0,0,0,294,295,1,0,0,0,295,296,1,0,0,0,
        296,297,5,36,0,0,297,49,1,0,0,0,298,299,5,1,0,0,299,51,1,0,0,0,300,
        301,5,2,0,0,301,53,1,0,0,0,302,304,7,2,0,0,303,302,1,0,0,0,303,304,
        1,0,0,0,304,305,1,0,0,0,305,306,5,34,0,0,306,55,1,0,0,0,33,59,72,
        84,89,105,117,123,127,136,149,164,168,175,188,192,200,207,210,217,
        226,235,238,245,248,254,261,264,273,279,286,289,294,303
    ]

class SmallerBasicParser ( Parser ):

    grammarFileName = "SmallerBasic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "'.'", "':'", "'+'", "'-'", "'*'", "'/'", 
                     "'>'", "'<'", "'='", "'>='", "'<='", "'<>'", "'And'", 
                     "'Or'", "'If'", "'Then'", "'Else'", "'EndIf'", "'While'", 
                     "'EndWhile'", "'For'", "'To'", "'Step'", "'EndFor'", 
                     "'Goto'", "'Sub'", "'EndSub'" ]

    symbolicNames = [ "<INVALID>", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "LROUND", "RROUND", "LSQUARE", "RSQUARE", "DOT", "COLON", 
                      "PLUS", "MINUS", "MUL", "DIV", "GT", "LT", "EQ", "GTEQ", 
                      "LTEQ", "NEQ", "AND", "OR", "IF", "THEN", "ELSE", 
                      "ENDIF", "WHILE", "ENDWHILE", "FOR", "TO", "STEP", 
                      "ENDFOR", "GOTO", "SUB", "ENDSUB", "ID", "INT", "FLOAT", 
                      "WS", "COMMENT", "NEWLINE", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declarationStatement = 2
    RULE_labelStatement = 3
    RULE_gotoStatement = 4
    RULE_ifStatement = 5
    RULE_whileStatement = 6
    RULE_forStatement = 7
    RULE_subroutineStatement = 8
    RULE_callSubroutineStatement = 9
    RULE_libraryStatement = 10
    RULE_expression = 11
    RULE_logicalExpression = 12
    RULE_booleanExpression = 13
    RULE_atomBoolean = 14
    RULE_arithmeticalExpression = 15
    RULE_additiveExpression = 16
    RULE_multiplicativeExpression = 17
    RULE_atomNumber = 18
    RULE_stringExpression = 19
    RULE_additiveStringExpression = 20
    RULE_atomString = 21
    RULE_literal = 22
    RULE_signedInt = 23
    RULE_signedFloat = 24
    RULE_string = 25
    RULE_boolean = 26
    RULE_signedId = 27

    ruleNames =  [ "program", "statement", "declarationStatement", "labelStatement", 
                   "gotoStatement", "ifStatement", "whileStatement", "forStatement", 
                   "subroutineStatement", "callSubroutineStatement", "libraryStatement", 
                   "expression", "logicalExpression", "booleanExpression", 
                   "atomBoolean", "arithmeticalExpression", "additiveExpression", 
                   "multiplicativeExpression", "atomNumber", "stringExpression", 
                   "additiveStringExpression", "atomString", "literal", 
                   "signedInt", "signedFloat", "string", "boolean", "signedId" ]

    EOF = Token.EOF
    STRING_LITERAL=1
    BOOLEAN_LITERAL=2
    LROUND=3
    RROUND=4
    LSQUARE=5
    RSQUARE=6
    DOT=7
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
    SUB=32
    ENDSUB=33
    ID=34
    INT=35
    FLOAT=36
    WS=37
    COMMENT=38
    NEWLINE=39
    LINE_COMMENT=40

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
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.statement()
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                    break

            self.state = 61
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


        def subroutineStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.SubroutineStatementContext,0)


        def callSubroutineStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.CallSubroutineStatementContext,0)


        def libraryStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.LibraryStatementContext,0)


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
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.declarationStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.whileStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.forStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 67
                self.labelStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 68
                self.gotoStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 69
                self.subroutineStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 70
                self.callSubroutineStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 71
                self.libraryStatement()
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


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_declarationStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayDeclarationStatementContext(DeclarationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.DeclarationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayDeclarationStatement" ):
                listener.enterArrayDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayDeclarationStatement" ):
                listener.exitArrayDeclarationStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDeclarationStatement" ):
                return visitor.visitArrayDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)


    class VariableDeclarationStatementContext(DeclarationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.DeclarationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)
        def EQ(self):
            return self.getToken(SmallerBasicParser.EQ, 0)
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



    def declarationStatement(self):

        localctx = SmallerBasicParser.DeclarationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declarationStatement)
        self._la = 0 # Token type
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.VariableDeclarationStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(SmallerBasicParser.ID)
                self.state = 75
                self.match(SmallerBasicParser.EQ)
                self.state = 76
                self.expression()
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.ArrayDeclarationStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(SmallerBasicParser.ID)
                self.state = 82 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 78
                    self.match(SmallerBasicParser.LSQUARE)
                    self.state = 79
                    self.arithmeticalExpression()
                    self.state = 80
                    self.match(SmallerBasicParser.RSQUARE)
                    self.state = 84 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==5):
                        break

                self.state = 86
                self.match(SmallerBasicParser.EQ)
                self.state = 87
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
            self.state = 91
            self.match(SmallerBasicParser.ID)
            self.state = 92
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
            self.state = 94
            self.match(SmallerBasicParser.GOTO)
            self.state = 95
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
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.match(SmallerBasicParser.IF)
                self.state = 98
                self.match(SmallerBasicParser.LROUND)
                self.state = 99
                self.logicalExpression()
                self.state = 100
                self.match(SmallerBasicParser.RROUND)
                self.state = 101
                self.match(SmallerBasicParser.THEN)
                self.state = 103 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 102
                    self.statement()
                    self.state = 105 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                        break

                self.state = 107
                self.match(SmallerBasicParser.ENDIF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(SmallerBasicParser.IF)
                self.state = 110
                self.match(SmallerBasicParser.LROUND)
                self.state = 111
                self.logicalExpression()
                self.state = 112
                self.match(SmallerBasicParser.RROUND)
                self.state = 113
                self.match(SmallerBasicParser.THEN)
                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 114
                    self.statement()
                    self.state = 117 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                        break

                self.state = 119
                self.match(SmallerBasicParser.ELSE)
                self.state = 121 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 120
                    self.statement()
                    self.state = 123 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                        break

                self.state = 125
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
            self.state = 129
            self.match(SmallerBasicParser.WHILE)
            self.state = 130
            self.match(SmallerBasicParser.LROUND)
            self.state = 131
            self.logicalExpression()
            self.state = 132
            self.match(SmallerBasicParser.RROUND)
            self.state = 134 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 133
                self.statement()
                self.state = 136 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                    break

            self.state = 138
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
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(SmallerBasicParser.FOR)
                self.state = 141
                self.match(SmallerBasicParser.ID)
                self.state = 142
                self.match(SmallerBasicParser.EQ)
                self.state = 143
                self.arithmeticalExpression()
                self.state = 144
                self.match(SmallerBasicParser.TO)
                self.state = 145
                self.arithmeticalExpression()
                self.state = 147 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 146
                    self.statement()
                    self.state = 149 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                        break

                self.state = 151
                self.match(SmallerBasicParser.ENDFOR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.match(SmallerBasicParser.FOR)
                self.state = 154
                self.match(SmallerBasicParser.ID)
                self.state = 155
                self.match(SmallerBasicParser.EQ)
                self.state = 156
                self.arithmeticalExpression()
                self.state = 157
                self.match(SmallerBasicParser.TO)
                self.state = 158
                self.arithmeticalExpression()
                self.state = 159
                self.match(SmallerBasicParser.STEP)
                self.state = 160
                self.arithmeticalExpression()
                self.state = 162 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 161
                    self.statement()
                    self.state = 164 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                        break

                self.state = 166
                self.match(SmallerBasicParser.ENDFOR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubroutineStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(SmallerBasicParser.SUB, 0)

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)

        def ENDSUB(self):
            return self.getToken(SmallerBasicParser.ENDSUB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.StatementContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.StatementContext,i)


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_subroutineStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubroutineStatement" ):
                listener.enterSubroutineStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubroutineStatement" ):
                listener.exitSubroutineStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubroutineStatement" ):
                return visitor.visitSubroutineStatement(self)
            else:
                return visitor.visitChildren(self)




    def subroutineStatement(self):

        localctx = SmallerBasicParser.SubroutineStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_subroutineStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(SmallerBasicParser.SUB)
            self.state = 171
            self.match(SmallerBasicParser.ID)
            self.state = 173 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 172
                self.statement()
                self.state = 175 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                    break

            self.state = 177
            self.match(SmallerBasicParser.ENDSUB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallSubroutineStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)

        def LROUND(self):
            return self.getToken(SmallerBasicParser.LROUND, 0)

        def RROUND(self):
            return self.getToken(SmallerBasicParser.RROUND, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_callSubroutineStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallSubroutineStatement" ):
                listener.enterCallSubroutineStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallSubroutineStatement" ):
                listener.exitCallSubroutineStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallSubroutineStatement" ):
                return visitor.visitCallSubroutineStatement(self)
            else:
                return visitor.visitChildren(self)




    def callSubroutineStatement(self):

        localctx = SmallerBasicParser.CallSubroutineStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_callSubroutineStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(SmallerBasicParser.ID)
            self.state = 180
            self.match(SmallerBasicParser.LROUND)
            self.state = 181
            self.match(SmallerBasicParser.RROUND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LibraryStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SmallerBasicParser.ID)
            else:
                return self.getToken(SmallerBasicParser.ID, i)

        def LROUND(self):
            return self.getToken(SmallerBasicParser.LROUND, 0)

        def RROUND(self):
            return self.getToken(SmallerBasicParser.RROUND, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(SmallerBasicParser.DOT)
            else:
                return self.getToken(SmallerBasicParser.DOT, i)

        def expression(self):
            return self.getTypedRuleContext(SmallerBasicParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_libraryStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLibraryStatement" ):
                listener.enterLibraryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLibraryStatement" ):
                listener.exitLibraryStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLibraryStatement" ):
                return visitor.visitLibraryStatement(self)
            else:
                return visitor.visitChildren(self)




    def libraryStatement(self):

        localctx = SmallerBasicParser.LibraryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_libraryStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(SmallerBasicParser.ID)
            self.state = 186 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 184
                self.match(SmallerBasicParser.DOT)
                self.state = 185
                self.match(SmallerBasicParser.ID)
                self.state = 188 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

            self.state = 190
            self.match(SmallerBasicParser.LROUND)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 120259085838) != 0):
                self.state = 191
                self.expression()


            self.state = 194
            self.match(SmallerBasicParser.RROUND)
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

        def literal(self):
            return self.getTypedRuleContext(SmallerBasicParser.LiteralContext,0)


        def logicalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.LogicalExpressionContext,0)


        def arithmeticalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.ArithmeticalExpressionContext,0)


        def stringExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.StringExpressionContext,0)


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
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.logicalExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 198
                self.arithmeticalExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 199
                self.stringExpression()
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
        self.enterRule(localctx, 24, self.RULE_logicalExpression)
        self._la = 0 # Token type
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.booleanExpression()
                self.state = 205 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 203
                    _la = self._input.LA(1)
                    if not(_la==19 or _la==20):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 204
                    self.booleanExpression()
                    self.state = 207 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==19 or _la==20):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
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
        self.enterRule(localctx, 26, self.RULE_booleanExpression)
        self._la = 0 # Token type
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.arithmeticalExpression()
                self.state = 213
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 214
                self.arithmeticalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
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


        def LROUND(self):
            return self.getToken(SmallerBasicParser.LROUND, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.LogicalExpressionContext,0)


        def RROUND(self):
            return self.getToken(SmallerBasicParser.RROUND, 0)

        def libraryStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.LibraryStatementContext,0)


        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)

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
        self.enterRule(localctx, 28, self.RULE_atomBoolean)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.boolean()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(SmallerBasicParser.LROUND)
                self.state = 221
                self.logicalExpression()
                self.state = 222
                self.match(SmallerBasicParser.RROUND)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 224
                self.libraryStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 225
                self.match(SmallerBasicParser.ID)
                pass


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
        self.enterRule(localctx, 30, self.RULE_arithmeticalExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
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
        self.enterRule(localctx, 32, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.multiplicativeExpression()
                self.state = 233 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 231
                    _la = self._input.LA(1)
                    if not(_la==9 or _la==10):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 232
                    self.multiplicativeExpression()
                    self.state = 235 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==9 or _la==10):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
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

        def atomNumber(self):
            return self.getTypedRuleContext(SmallerBasicParser.AtomNumberContext,0)


        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.MultiplicativeExpressionContext,i)


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
        self.enterRule(localctx, 34, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.atomNumber()
                self.state = 243 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 241
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 242
                        self.multiplicativeExpression()

                    else:
                        raise NoViableAltException(self)
                    self.state = 245 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
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

        def signedInt(self):
            return self.getTypedRuleContext(SmallerBasicParser.SignedIntContext,0)


        def signedFloat(self):
            return self.getTypedRuleContext(SmallerBasicParser.SignedFloatContext,0)


        def signedId(self):
            return self.getTypedRuleContext(SmallerBasicParser.SignedIdContext,0)


        def LROUND(self):
            return self.getToken(SmallerBasicParser.LROUND, 0)

        def arithmeticalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.ArithmeticalExpressionContext,0)


        def RROUND(self):
            return self.getToken(SmallerBasicParser.RROUND, 0)

        def MINUS(self):
            return self.getToken(SmallerBasicParser.MINUS, 0)

        def libraryStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.LibraryStatementContext,0)


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
        self.enterRule(localctx, 36, self.RULE_atomNumber)
        self._la = 0 # Token type
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.signedInt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.signedFloat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.signedId()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 253
                    self.match(SmallerBasicParser.MINUS)


                self.state = 256
                self.match(SmallerBasicParser.LROUND)
                self.state = 257
                self.arithmeticalExpression()
                self.state = 258
                self.match(SmallerBasicParser.RROUND)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 260
                    self.match(SmallerBasicParser.MINUS)


                self.state = 263
                self.libraryStatement()
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
        self.enterRule(localctx, 38, self.RULE_stringExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
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

        def atomString(self):
            return self.getTypedRuleContext(SmallerBasicParser.AtomStringContext,0)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(SmallerBasicParser.PLUS)
            else:
                return self.getToken(SmallerBasicParser.PLUS, i)

        def additiveStringExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.AdditiveStringExpressionContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.AdditiveStringExpressionContext,i)


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
        self.enterRule(localctx, 40, self.RULE_additiveStringExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.atomString()
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 269
                    self.match(SmallerBasicParser.PLUS)
                    self.state = 270
                    self.additiveStringExpression() 
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_atomString

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AtomStringIdContext(AtomStringContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomStringContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomStringId" ):
                listener.enterAtomStringId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomStringId" ):
                listener.exitAtomStringId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomStringId" ):
                return visitor.visitAtomStringId(self)
            else:
                return visitor.visitChildren(self)


    class AtomStringLibraryStatementContext(AtomStringContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomStringContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def libraryStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.LibraryStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomStringLibraryStatement" ):
                listener.enterAtomStringLibraryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomStringLibraryStatement" ):
                listener.exitAtomStringLibraryStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomStringLibraryStatement" ):
                return visitor.visitAtomStringLibraryStatement(self)
            else:
                return visitor.visitChildren(self)


    class AtomStringLiteralContext(AtomStringContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomStringContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def string(self):
            return self.getTypedRuleContext(SmallerBasicParser.StringContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomStringLiteral" ):
                listener.enterAtomStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomStringLiteral" ):
                listener.exitAtomStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomStringLiteral" ):
                return visitor.visitAtomStringLiteral(self)
            else:
                return visitor.visitChildren(self)



    def atomString(self):

        localctx = SmallerBasicParser.AtomStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_atomString)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.AtomStringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.string()
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.AtomStringIdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(SmallerBasicParser.ID)
                pass

            elif la_ == 3:
                localctx = SmallerBasicParser.AtomStringLibraryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 278
                self.libraryStatement()
                pass


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

        def signedInt(self):
            return self.getTypedRuleContext(SmallerBasicParser.SignedIntContext,0)


        def signedFloat(self):
            return self.getTypedRuleContext(SmallerBasicParser.SignedFloatContext,0)


        def string(self):
            return self.getTypedRuleContext(SmallerBasicParser.StringContext,0)


        def boolean(self):
            return self.getTypedRuleContext(SmallerBasicParser.BooleanContext,0)


        def signedId(self):
            return self.getTypedRuleContext(SmallerBasicParser.SignedIdContext,0)


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
        self.enterRule(localctx, 44, self.RULE_literal)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.signedInt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.signedFloat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.string()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 284
                self.boolean()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 285
                self.signedId()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignedIntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SmallerBasicParser.INT, 0)

        def MINUS(self):
            return self.getToken(SmallerBasicParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(SmallerBasicParser.PLUS, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_signedInt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignedInt" ):
                listener.enterSignedInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignedInt" ):
                listener.exitSignedInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignedInt" ):
                return visitor.visitSignedInt(self)
            else:
                return visitor.visitChildren(self)




    def signedInt(self):

        localctx = SmallerBasicParser.SignedIntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_signedInt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9 or _la==10:
                self.state = 288
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 291
            self.match(SmallerBasicParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignedFloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(SmallerBasicParser.FLOAT, 0)

        def MINUS(self):
            return self.getToken(SmallerBasicParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(SmallerBasicParser.PLUS, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_signedFloat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignedFloat" ):
                listener.enterSignedFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignedFloat" ):
                listener.exitSignedFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignedFloat" ):
                return visitor.visitSignedFloat(self)
            else:
                return visitor.visitChildren(self)




    def signedFloat(self):

        localctx = SmallerBasicParser.SignedFloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_signedFloat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9 or _la==10:
                self.state = 293
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 296
            self.match(SmallerBasicParser.FLOAT)
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
        self.enterRule(localctx, 50, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
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
        self.enterRule(localctx, 52, self.RULE_boolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(SmallerBasicParser.BOOLEAN_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignedIdContext(ParserRuleContext):
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
            return SmallerBasicParser.RULE_signedId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignedId" ):
                listener.enterSignedId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignedId" ):
                listener.exitSignedId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignedId" ):
                return visitor.visitSignedId(self)
            else:
                return visitor.visitChildren(self)




    def signedId(self):

        localctx = SmallerBasicParser.SignedIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_signedId)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9 or _la==10:
                self.state = 302
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 305
            self.match(SmallerBasicParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





