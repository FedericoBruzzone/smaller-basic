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
        4,1,41,308,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,4,0,50,8,0,11,0,12,0,51,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,65,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,4,2,75,8,2,11,2,12,2,76,1,2,1,2,1,2,3,2,82,8,
        2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,4,5,96,8,5,11,
        5,12,5,97,3,5,100,8,5,1,5,1,5,4,5,104,8,5,11,5,12,5,105,3,5,108,
        8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,4,5,118,8,5,11,5,12,5,119,3,
        5,122,8,5,1,5,1,5,3,5,126,8,5,1,6,1,6,1,6,1,6,1,6,4,6,133,8,6,11,
        6,12,6,134,3,6,137,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,4,7,148,
        8,7,11,7,12,7,149,3,7,152,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,4,7,165,8,7,11,7,12,7,166,3,7,169,8,7,1,7,1,7,3,7,173,
        8,7,1,8,1,8,1,8,4,8,178,8,8,11,8,12,8,179,3,8,182,8,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,197,8,10,10,
        10,12,10,200,9,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,209,8,
        10,1,11,1,11,1,11,1,11,1,11,4,11,216,8,11,11,11,12,11,217,1,12,1,
        12,1,12,3,12,223,8,12,1,13,1,13,1,13,5,13,228,8,13,10,13,12,13,231,
        9,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,242,8,14,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,252,8,15,1,16,1,16,
        1,17,1,17,1,17,5,17,259,8,17,10,17,12,17,262,9,17,1,18,1,18,1,18,
        5,18,267,8,18,10,18,12,18,270,9,18,1,19,3,19,273,8,19,1,19,1,19,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,286,8,20,1,21,
        1,21,1,22,1,22,1,22,5,22,293,8,22,10,22,12,22,296,9,22,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,3,23,306,8,23,1,23,0,0,24,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,4,1,
        0,20,21,1,0,14,19,1,0,10,11,1,0,12,13,335,0,49,1,0,0,0,2,64,1,0,
        0,0,4,81,1,0,0,0,6,83,1,0,0,0,8,86,1,0,0,0,10,125,1,0,0,0,12,127,
        1,0,0,0,14,172,1,0,0,0,16,174,1,0,0,0,18,185,1,0,0,0,20,208,1,0,
        0,0,22,210,1,0,0,0,24,222,1,0,0,0,26,224,1,0,0,0,28,241,1,0,0,0,
        30,251,1,0,0,0,32,253,1,0,0,0,34,255,1,0,0,0,36,263,1,0,0,0,38,272,
        1,0,0,0,40,285,1,0,0,0,42,287,1,0,0,0,44,289,1,0,0,0,46,305,1,0,
        0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,
        1,0,0,0,52,53,1,0,0,0,53,54,5,0,0,1,54,1,1,0,0,0,55,65,3,4,2,0,56,
        65,3,12,6,0,57,65,3,14,7,0,58,65,3,10,5,0,59,65,3,6,3,0,60,65,3,
        8,4,0,61,65,3,16,8,0,62,65,3,18,9,0,63,65,3,20,10,0,64,55,1,0,0,
        0,64,56,1,0,0,0,64,57,1,0,0,0,64,58,1,0,0,0,64,59,1,0,0,0,64,60,
        1,0,0,0,64,61,1,0,0,0,64,62,1,0,0,0,64,63,1,0,0,0,65,3,1,0,0,0,66,
        67,5,35,0,0,67,68,5,16,0,0,68,82,3,24,12,0,69,74,5,35,0,0,70,71,
        5,5,0,0,71,72,3,32,16,0,72,73,5,6,0,0,73,75,1,0,0,0,74,70,1,0,0,
        0,75,76,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,79,
        5,16,0,0,79,80,3,24,12,0,80,82,1,0,0,0,81,66,1,0,0,0,81,69,1,0,0,
        0,82,5,1,0,0,0,83,84,5,35,0,0,84,85,5,8,0,0,85,7,1,0,0,0,86,87,5,
        32,0,0,87,88,5,35,0,0,88,9,1,0,0,0,89,90,5,22,0,0,90,91,5,3,0,0,
        91,92,3,26,13,0,92,93,5,4,0,0,93,99,5,23,0,0,94,96,3,2,1,0,95,94,
        1,0,0,0,96,97,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,
        99,95,1,0,0,0,99,100,1,0,0,0,100,101,1,0,0,0,101,107,5,24,0,0,102,
        104,3,2,1,0,103,102,1,0,0,0,104,105,1,0,0,0,105,103,1,0,0,0,105,
        106,1,0,0,0,106,108,1,0,0,0,107,103,1,0,0,0,107,108,1,0,0,0,108,
        109,1,0,0,0,109,110,5,25,0,0,110,126,1,0,0,0,111,112,5,22,0,0,112,
        113,5,3,0,0,113,114,3,26,13,0,114,115,5,4,0,0,115,121,5,23,0,0,116,
        118,3,2,1,0,117,116,1,0,0,0,118,119,1,0,0,0,119,117,1,0,0,0,119,
        120,1,0,0,0,120,122,1,0,0,0,121,117,1,0,0,0,121,122,1,0,0,0,122,
        123,1,0,0,0,123,124,5,25,0,0,124,126,1,0,0,0,125,89,1,0,0,0,125,
        111,1,0,0,0,126,11,1,0,0,0,127,128,5,26,0,0,128,129,5,3,0,0,129,
        130,3,26,13,0,130,136,5,4,0,0,131,133,3,2,1,0,132,131,1,0,0,0,133,
        134,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,137,1,0,0,0,136,
        132,1,0,0,0,136,137,1,0,0,0,137,138,1,0,0,0,138,139,5,27,0,0,139,
        13,1,0,0,0,140,141,5,28,0,0,141,142,5,35,0,0,142,143,5,16,0,0,143,
        144,3,32,16,0,144,145,5,29,0,0,145,151,3,32,16,0,146,148,3,2,1,0,
        147,146,1,0,0,0,148,149,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,
        150,152,1,0,0,0,151,147,1,0,0,0,151,152,1,0,0,0,152,153,1,0,0,0,
        153,154,5,31,0,0,154,173,1,0,0,0,155,156,5,28,0,0,156,157,5,35,0,
        0,157,158,5,16,0,0,158,159,3,32,16,0,159,160,5,29,0,0,160,161,3,
        32,16,0,161,162,5,30,0,0,162,168,3,32,16,0,163,165,3,2,1,0,164,163,
        1,0,0,0,165,166,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,169,
        1,0,0,0,168,164,1,0,0,0,168,169,1,0,0,0,169,170,1,0,0,0,170,171,
        5,31,0,0,171,173,1,0,0,0,172,140,1,0,0,0,172,155,1,0,0,0,173,15,
        1,0,0,0,174,175,5,33,0,0,175,181,5,35,0,0,176,178,3,2,1,0,177,176,
        1,0,0,0,178,179,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,182,
        1,0,0,0,181,177,1,0,0,0,181,182,1,0,0,0,182,183,1,0,0,0,183,184,
        5,34,0,0,184,17,1,0,0,0,185,186,5,35,0,0,186,187,5,3,0,0,187,188,
        5,4,0,0,188,19,1,0,0,0,189,190,5,35,0,0,190,191,5,7,0,0,191,192,
        5,35,0,0,192,193,5,3,0,0,193,198,3,24,12,0,194,195,5,9,0,0,195,197,
        3,24,12,0,196,194,1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,
        1,0,0,0,199,201,1,0,0,0,200,198,1,0,0,0,201,202,5,4,0,0,202,209,
        1,0,0,0,203,204,5,35,0,0,204,205,5,7,0,0,205,206,5,35,0,0,206,207,
        5,3,0,0,207,209,5,4,0,0,208,189,1,0,0,0,208,203,1,0,0,0,209,21,1,
        0,0,0,210,215,5,35,0,0,211,212,5,5,0,0,212,213,3,32,16,0,213,214,
        5,6,0,0,214,216,1,0,0,0,215,211,1,0,0,0,216,217,1,0,0,0,217,215,
        1,0,0,0,217,218,1,0,0,0,218,23,1,0,0,0,219,223,3,26,13,0,220,223,
        3,32,16,0,221,223,3,42,21,0,222,219,1,0,0,0,222,220,1,0,0,0,222,
        221,1,0,0,0,223,25,1,0,0,0,224,229,3,28,14,0,225,226,7,0,0,0,226,
        228,3,28,14,0,227,225,1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,
        230,1,0,0,0,230,27,1,0,0,0,231,229,1,0,0,0,232,233,3,32,16,0,233,
        234,7,1,0,0,234,235,3,32,16,0,235,242,1,0,0,0,236,237,3,42,21,0,
        237,238,7,1,0,0,238,239,3,42,21,0,239,242,1,0,0,0,240,242,3,30,15,
        0,241,232,1,0,0,0,241,236,1,0,0,0,241,240,1,0,0,0,242,29,1,0,0,0,
        243,252,5,2,0,0,244,252,5,35,0,0,245,246,5,3,0,0,246,247,3,26,13,
        0,247,248,5,4,0,0,248,252,1,0,0,0,249,252,3,20,10,0,250,252,3,22,
        11,0,251,243,1,0,0,0,251,244,1,0,0,0,251,245,1,0,0,0,251,249,1,0,
        0,0,251,250,1,0,0,0,252,31,1,0,0,0,253,254,3,34,17,0,254,33,1,0,
        0,0,255,260,3,36,18,0,256,257,7,2,0,0,257,259,3,36,18,0,258,256,
        1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,35,1,
        0,0,0,262,260,1,0,0,0,263,268,3,38,19,0,264,265,7,3,0,0,265,267,
        3,36,18,0,266,264,1,0,0,0,267,270,1,0,0,0,268,266,1,0,0,0,268,269,
        1,0,0,0,269,37,1,0,0,0,270,268,1,0,0,0,271,273,7,2,0,0,272,271,1,
        0,0,0,272,273,1,0,0,0,273,274,1,0,0,0,274,275,3,40,20,0,275,39,1,
        0,0,0,276,286,5,36,0,0,277,286,5,37,0,0,278,286,5,35,0,0,279,280,
        5,3,0,0,280,281,3,34,17,0,281,282,5,4,0,0,282,286,1,0,0,0,283,286,
        3,20,10,0,284,286,3,22,11,0,285,276,1,0,0,0,285,277,1,0,0,0,285,
        278,1,0,0,0,285,279,1,0,0,0,285,283,1,0,0,0,285,284,1,0,0,0,286,
        41,1,0,0,0,287,288,3,44,22,0,288,43,1,0,0,0,289,294,3,46,23,0,290,
        291,5,10,0,0,291,293,3,44,22,0,292,290,1,0,0,0,293,296,1,0,0,0,294,
        292,1,0,0,0,294,295,1,0,0,0,295,45,1,0,0,0,296,294,1,0,0,0,297,306,
        5,1,0,0,298,306,5,35,0,0,299,300,5,3,0,0,300,301,3,42,21,0,301,302,
        5,4,0,0,302,306,1,0,0,0,303,306,3,20,10,0,304,306,3,22,11,0,305,
        297,1,0,0,0,305,298,1,0,0,0,305,299,1,0,0,0,305,303,1,0,0,0,305,
        304,1,0,0,0,306,47,1,0,0,0,33,51,64,76,81,97,99,105,107,119,121,
        125,134,136,149,151,166,168,172,179,181,198,208,217,222,229,241,
        251,260,268,272,285,294,305
    ]

class SmallerBasicParser ( Parser ):

    grammarFileName = "SmallerBasic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "'.'", "':'", "','", "'+'", "'-'", "'*'", 
                     "'/'", "'>'", "'<'", "'='", "'>='", "'<='", "'<>'", 
                     "'And'", "'Or'", "'If'", "'Then'", "'Else'", "'EndIf'", 
                     "'While'", "'EndWhile'", "'For'", "'To'", "'Step'", 
                     "'EndFor'", "'Goto'", "'Sub'", "'EndSub'" ]

    symbolicNames = [ "<INVALID>", "STRING", "BOOLEAN", "LROUND", "RROUND", 
                      "LSQUARE", "RSQUARE", "DOT", "COLON", "COMMA", "PLUS", 
                      "MINUS", "MUL", "DIV", "GT", "LT", "EQ", "GTEQ", "LTEQ", 
                      "NEQ", "AND", "OR", "IF", "THEN", "ELSE", "ENDIF", 
                      "WHILE", "ENDWHILE", "FOR", "TO", "STEP", "ENDFOR", 
                      "GOTO", "SUB", "ENDSUB", "ID", "INT", "FLOAT", "WS", 
                      "NEWLINE", "LINE_COMMENT", "COMMENT" ]

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
    RULE_arrayAccess = 11
    RULE_expression = 12
    RULE_logicalExpression = 13
    RULE_booleanExpression = 14
    RULE_atomBoolean = 15
    RULE_arithmeticalExpression = 16
    RULE_additiveExpression = 17
    RULE_multiplicativeExpression = 18
    RULE_unaryAtomNumber = 19
    RULE_atomNumber = 20
    RULE_stringExpression = 21
    RULE_additiveStringExpression = 22
    RULE_atomString = 23

    ruleNames =  [ "program", "statement", "declarationStatement", "labelStatement", 
                   "gotoStatement", "ifStatement", "whileStatement", "forStatement", 
                   "subroutineStatement", "callSubroutineStatement", "libraryStatement", 
                   "arrayAccess", "expression", "logicalExpression", "booleanExpression", 
                   "atomBoolean", "arithmeticalExpression", "additiveExpression", 
                   "multiplicativeExpression", "unaryAtomNumber", "atomNumber", 
                   "stringExpression", "additiveStringExpression", "atomString" ]

    EOF = Token.EOF
    STRING=1
    BOOLEAN=2
    LROUND=3
    RROUND=4
    LSQUARE=5
    RSQUARE=6
    DOT=7
    COLON=8
    COMMA=9
    PLUS=10
    MINUS=11
    MUL=12
    DIV=13
    GT=14
    LT=15
    EQ=16
    GTEQ=17
    LTEQ=18
    NEQ=19
    AND=20
    OR=21
    IF=22
    THEN=23
    ELSE=24
    ENDIF=25
    WHILE=26
    ENDWHILE=27
    FOR=28
    TO=29
    STEP=30
    ENDFOR=31
    GOTO=32
    SUB=33
    ENDSUB=34
    ID=35
    INT=36
    FLOAT=37
    WS=38
    NEWLINE=39
    LINE_COMMENT=40
    COMMENT=41

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0)):
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
            self.state = 64
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

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 61
                self.subroutineStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 62
                self.callSubroutineStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 63
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
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.VariableDeclarationStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(SmallerBasicParser.ID)
                self.state = 67
                self.match(SmallerBasicParser.EQ)
                self.state = 68
                self.expression()
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.ArrayDeclarationStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(SmallerBasicParser.ID)
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 70
                    self.match(SmallerBasicParser.LSQUARE)
                    self.state = 71
                    self.arithmeticalExpression()
                    self.state = 72
                    self.match(SmallerBasicParser.RSQUARE)
                    self.state = 76 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==5):
                        break

                self.state = 78
                self.match(SmallerBasicParser.EQ)
                self.state = 79
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
            self.state = 83
            self.match(SmallerBasicParser.ID)
            self.state = 84
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
            self.state = 86
            self.match(SmallerBasicParser.GOTO)
            self.state = 87
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


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_ifStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfStatementWithElseContext(IfStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.IfStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

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
        def ELSE(self):
            return self.getToken(SmallerBasicParser.ELSE, 0)
        def ENDIF(self):
            return self.getToken(SmallerBasicParser.ENDIF, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.StatementContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatementWithElse" ):
                listener.enterIfStatementWithElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatementWithElse" ):
                listener.exitIfStatementWithElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatementWithElse" ):
                return visitor.visitIfStatementWithElse(self)
            else:
                return visitor.visitChildren(self)


    class IfStatementWithoutElseContext(IfStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.IfStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatementWithoutElse" ):
                listener.enterIfStatementWithoutElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatementWithoutElse" ):
                listener.exitIfStatementWithoutElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatementWithoutElse" ):
                return visitor.visitIfStatementWithoutElse(self)
            else:
                return visitor.visitChildren(self)



    def ifStatement(self):

        localctx = SmallerBasicParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.IfStatementWithElseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(SmallerBasicParser.IF)
                self.state = 90
                self.match(SmallerBasicParser.LROUND)
                self.state = 91
                self.logicalExpression()
                self.state = 92
                self.match(SmallerBasicParser.RROUND)
                self.state = 93
                self.match(SmallerBasicParser.THEN)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0):
                    self.state = 95 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 94
                        self.statement()
                        self.state = 97 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0)):
                            break



                self.state = 101
                self.match(SmallerBasicParser.ELSE)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0):
                    self.state = 103 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 102
                        self.statement()
                        self.state = 105 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0)):
                            break



                self.state = 109
                self.match(SmallerBasicParser.ENDIF)
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.IfStatementWithoutElseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(SmallerBasicParser.IF)
                self.state = 112
                self.match(SmallerBasicParser.LROUND)
                self.state = 113
                self.logicalExpression()
                self.state = 114
                self.match(SmallerBasicParser.RROUND)
                self.state = 115
                self.match(SmallerBasicParser.THEN)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0):
                    self.state = 117 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 116
                        self.statement()
                        self.state = 119 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0)):
                            break



                self.state = 123
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


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_whileStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileStatementStandardContext(WhileStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.WhileStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatementStandard" ):
                listener.enterWhileStatementStandard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatementStandard" ):
                listener.exitWhileStatementStandard(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatementStandard" ):
                return visitor.visitWhileStatementStandard(self)
            else:
                return visitor.visitChildren(self)



    def whileStatement(self):

        localctx = SmallerBasicParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            localctx = SmallerBasicParser.WhileStatementStandardContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(SmallerBasicParser.WHILE)
            self.state = 128
            self.match(SmallerBasicParser.LROUND)
            self.state = 129
            self.logicalExpression()
            self.state = 130
            self.match(SmallerBasicParser.RROUND)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0):
                self.state = 132 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 131
                    self.statement()
                    self.state = 134 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0)):
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


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_forStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForStatementWithStepContext(ForStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.ForStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

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
        def STEP(self):
            return self.getToken(SmallerBasicParser.STEP, 0)
        def ENDFOR(self):
            return self.getToken(SmallerBasicParser.ENDFOR, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.StatementContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatementWithStep" ):
                listener.enterForStatementWithStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatementWithStep" ):
                listener.exitForStatementWithStep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatementWithStep" ):
                return visitor.visitForStatementWithStep(self)
            else:
                return visitor.visitChildren(self)


    class ForStatementStandardContext(ForStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.ForStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatementStandard" ):
                listener.enterForStatementStandard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatementStandard" ):
                listener.exitForStatementStandard(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatementStandard" ):
                return visitor.visitForStatementStandard(self)
            else:
                return visitor.visitChildren(self)



    def forStatement(self):

        localctx = SmallerBasicParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.ForStatementStandardContext(self, localctx)
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
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0):
                    self.state = 147 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 146
                        self.statement()
                        self.state = 149 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0)):
                            break



                self.state = 153
                self.match(SmallerBasicParser.ENDFOR)
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.ForStatementWithStepContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(SmallerBasicParser.FOR)
                self.state = 156
                self.match(SmallerBasicParser.ID)
                self.state = 157
                self.match(SmallerBasicParser.EQ)
                self.state = 158
                self.arithmeticalExpression()
                self.state = 159
                self.match(SmallerBasicParser.TO)
                self.state = 160
                self.arithmeticalExpression()
                self.state = 161
                self.match(SmallerBasicParser.STEP)
                self.state = 162
                self.arithmeticalExpression()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0):
                    self.state = 164 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 163
                        self.statement()
                        self.state = 166 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0)):
                            break



                self.state = 170
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


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_subroutineStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SubroutineStatementStandardContext(SubroutineStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.SubroutineStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubroutineStatementStandard" ):
                listener.enterSubroutineStatementStandard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubroutineStatementStandard" ):
                listener.exitSubroutineStatementStandard(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubroutineStatementStandard" ):
                return visitor.visitSubroutineStatementStandard(self)
            else:
                return visitor.visitChildren(self)



    def subroutineStatement(self):

        localctx = SmallerBasicParser.SubroutineStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_subroutineStatement)
        self._la = 0 # Token type
        try:
            localctx = SmallerBasicParser.SubroutineStatementStandardContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(SmallerBasicParser.SUB)
            self.state = 175
            self.match(SmallerBasicParser.ID)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0):
                self.state = 177 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 176
                    self.statement()
                    self.state = 179 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0)):
                        break



            self.state = 183
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


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_callSubroutineStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CallSubroutineStatementStandardContext(CallSubroutineStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.CallSubroutineStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)
        def LROUND(self):
            return self.getToken(SmallerBasicParser.LROUND, 0)
        def RROUND(self):
            return self.getToken(SmallerBasicParser.RROUND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallSubroutineStatementStandard" ):
                listener.enterCallSubroutineStatementStandard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallSubroutineStatementStandard" ):
                listener.exitCallSubroutineStatementStandard(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallSubroutineStatementStandard" ):
                return visitor.visitCallSubroutineStatementStandard(self)
            else:
                return visitor.visitChildren(self)



    def callSubroutineStatement(self):

        localctx = SmallerBasicParser.CallSubroutineStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_callSubroutineStatement)
        try:
            localctx = SmallerBasicParser.CallSubroutineStatementStandardContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(SmallerBasicParser.ID)
            self.state = 186
            self.match(SmallerBasicParser.LROUND)
            self.state = 187
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


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_libraryStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LibraryStatementWithParametersContext(LibraryStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.LibraryStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SmallerBasicParser.ID)
            else:
                return self.getToken(SmallerBasicParser.ID, i)
        def DOT(self):
            return self.getToken(SmallerBasicParser.DOT, 0)
        def LROUND(self):
            return self.getToken(SmallerBasicParser.LROUND, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.ExpressionContext,i)

        def RROUND(self):
            return self.getToken(SmallerBasicParser.RROUND, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SmallerBasicParser.COMMA)
            else:
                return self.getToken(SmallerBasicParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLibraryStatementWithParameters" ):
                listener.enterLibraryStatementWithParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLibraryStatementWithParameters" ):
                listener.exitLibraryStatementWithParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLibraryStatementWithParameters" ):
                return visitor.visitLibraryStatementWithParameters(self)
            else:
                return visitor.visitChildren(self)


    class LibraryStatementWithoutParametersContext(LibraryStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.LibraryStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SmallerBasicParser.ID)
            else:
                return self.getToken(SmallerBasicParser.ID, i)
        def DOT(self):
            return self.getToken(SmallerBasicParser.DOT, 0)
        def LROUND(self):
            return self.getToken(SmallerBasicParser.LROUND, 0)
        def RROUND(self):
            return self.getToken(SmallerBasicParser.RROUND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLibraryStatementWithoutParameters" ):
                listener.enterLibraryStatementWithoutParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLibraryStatementWithoutParameters" ):
                listener.exitLibraryStatementWithoutParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLibraryStatementWithoutParameters" ):
                return visitor.visitLibraryStatementWithoutParameters(self)
            else:
                return visitor.visitChildren(self)



    def libraryStatement(self):

        localctx = SmallerBasicParser.LibraryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_libraryStatement)
        self._la = 0 # Token type
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.LibraryStatementWithParametersContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(SmallerBasicParser.ID)
                self.state = 190
                self.match(SmallerBasicParser.DOT)
                self.state = 191
                self.match(SmallerBasicParser.ID)
                self.state = 192
                self.match(SmallerBasicParser.LROUND)
                self.state = 193
                self.expression()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 194
                    self.match(SmallerBasicParser.COMMA)
                    self.state = 195
                    self.expression()
                    self.state = 200
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 201
                self.match(SmallerBasicParser.RROUND)
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.LibraryStatementWithoutParametersContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(SmallerBasicParser.ID)
                self.state = 204
                self.match(SmallerBasicParser.DOT)
                self.state = 205
                self.match(SmallerBasicParser.ID)
                self.state = 206
                self.match(SmallerBasicParser.LROUND)
                self.state = 207
                self.match(SmallerBasicParser.RROUND)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_arrayAccess

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayAccessStandardContext(ArrayAccessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.ArrayAccessContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)
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
            if hasattr( listener, "enterArrayAccessStandard" ):
                listener.enterArrayAccessStandard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccessStandard" ):
                listener.exitArrayAccessStandard(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccessStandard" ):
                return visitor.visitArrayAccessStandard(self)
            else:
                return visitor.visitChildren(self)



    def arrayAccess(self):

        localctx = SmallerBasicParser.ArrayAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrayAccess)
        self._la = 0 # Token type
        try:
            localctx = SmallerBasicParser.ArrayAccessStandardContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(SmallerBasicParser.ID)
            self.state = 215 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 211
                self.match(SmallerBasicParser.LSQUARE)
                self.state = 212
                self.arithmeticalExpression()
                self.state = 213
                self.match(SmallerBasicParser.RSQUARE)
                self.state = 217 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5):
                    break

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
        self.enterRule(localctx, 24, self.RULE_expression)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.logicalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.arithmeticalExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
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
        self.enterRule(localctx, 26, self.RULE_logicalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.booleanExpression()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==21:
                self.state = 225
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 226
                self.booleanExpression()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_booleanExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BooleanStringExpressionContext(BooleanExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.BooleanExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stringExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SmallerBasicParser.StringExpressionContext)
            else:
                return self.getTypedRuleContext(SmallerBasicParser.StringExpressionContext,i)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanStringExpression" ):
                listener.enterBooleanStringExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanStringExpression" ):
                listener.exitBooleanStringExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanStringExpression" ):
                return visitor.visitBooleanStringExpression(self)
            else:
                return visitor.visitChildren(self)


    class BooleanAtomExpressionContext(BooleanExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.BooleanExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomBoolean(self):
            return self.getTypedRuleContext(SmallerBasicParser.AtomBooleanContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanAtomExpression" ):
                listener.enterBooleanAtomExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanAtomExpression" ):
                listener.exitBooleanAtomExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanAtomExpression" ):
                return visitor.visitBooleanAtomExpression(self)
            else:
                return visitor.visitChildren(self)


    class BooleanArithmeticalExpressionContext(BooleanExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.BooleanExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanArithmeticalExpression" ):
                listener.enterBooleanArithmeticalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanArithmeticalExpression" ):
                listener.exitBooleanArithmeticalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanArithmeticalExpression" ):
                return visitor.visitBooleanArithmeticalExpression(self)
            else:
                return visitor.visitChildren(self)



    def booleanExpression(self):

        localctx = SmallerBasicParser.BooleanExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_booleanExpression)
        self._la = 0 # Token type
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.BooleanArithmeticalExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.arithmeticalExpression()
                self.state = 233
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 234
                self.arithmeticalExpression()
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.BooleanStringExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.stringExpression()
                self.state = 237
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 238
                self.stringExpression()
                pass

            elif la_ == 3:
                localctx = SmallerBasicParser.BooleanAtomExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 240
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


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_atomBoolean

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AtomBooleanParenthesisContext(AtomBooleanContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomBooleanContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LROUND(self):
            return self.getToken(SmallerBasicParser.LROUND, 0)
        def logicalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.LogicalExpressionContext,0)

        def RROUND(self):
            return self.getToken(SmallerBasicParser.RROUND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomBooleanParenthesis" ):
                listener.enterAtomBooleanParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomBooleanParenthesis" ):
                listener.exitAtomBooleanParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomBooleanParenthesis" ):
                return visitor.visitAtomBooleanParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class AtomBooleanLibraryStatementContext(AtomBooleanContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomBooleanContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def libraryStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.LibraryStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomBooleanLibraryStatement" ):
                listener.enterAtomBooleanLibraryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomBooleanLibraryStatement" ):
                listener.exitAtomBooleanLibraryStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomBooleanLibraryStatement" ):
                return visitor.visitAtomBooleanLibraryStatement(self)
            else:
                return visitor.visitChildren(self)


    class AtomBooleanIdContext(AtomBooleanContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomBooleanContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomBooleanId" ):
                listener.enterAtomBooleanId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomBooleanId" ):
                listener.exitAtomBooleanId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomBooleanId" ):
                return visitor.visitAtomBooleanId(self)
            else:
                return visitor.visitChildren(self)


    class AtomBooleanBooleanContext(AtomBooleanContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomBooleanContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(SmallerBasicParser.BOOLEAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomBooleanBoolean" ):
                listener.enterAtomBooleanBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomBooleanBoolean" ):
                listener.exitAtomBooleanBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomBooleanBoolean" ):
                return visitor.visitAtomBooleanBoolean(self)
            else:
                return visitor.visitChildren(self)


    class AtomBooleanArrayAccessContext(AtomBooleanContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomBooleanContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arrayAccess(self):
            return self.getTypedRuleContext(SmallerBasicParser.ArrayAccessContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomBooleanArrayAccess" ):
                listener.enterAtomBooleanArrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomBooleanArrayAccess" ):
                listener.exitAtomBooleanArrayAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomBooleanArrayAccess" ):
                return visitor.visitAtomBooleanArrayAccess(self)
            else:
                return visitor.visitChildren(self)



    def atomBoolean(self):

        localctx = SmallerBasicParser.AtomBooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_atomBoolean)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.AtomBooleanBooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(SmallerBasicParser.BOOLEAN)
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.AtomBooleanIdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(SmallerBasicParser.ID)
                pass

            elif la_ == 3:
                localctx = SmallerBasicParser.AtomBooleanParenthesisContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 245
                self.match(SmallerBasicParser.LROUND)
                self.state = 246
                self.logicalExpression()
                self.state = 247
                self.match(SmallerBasicParser.RROUND)
                pass

            elif la_ == 4:
                localctx = SmallerBasicParser.AtomBooleanLibraryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 249
                self.libraryStatement()
                pass

            elif la_ == 5:
                localctx = SmallerBasicParser.AtomBooleanArrayAccessContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 250
                self.arrayAccess()
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
        self.enterRule(localctx, 32, self.RULE_arithmeticalExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
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
        self.enterRule(localctx, 34, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.multiplicativeExpression()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==11:
                self.state = 256
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 257
                self.multiplicativeExpression()
                self.state = 262
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

        def unaryAtomNumber(self):
            return self.getTypedRuleContext(SmallerBasicParser.UnaryAtomNumberContext,0)


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
        self.enterRule(localctx, 36, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.unaryAtomNumber()
            self.state = 268
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 264
                    _la = self._input.LA(1)
                    if not(_la==12 or _la==13):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 265
                    self.multiplicativeExpression() 
                self.state = 270
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryAtomNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomNumber(self):
            return self.getTypedRuleContext(SmallerBasicParser.AtomNumberContext,0)


        def PLUS(self):
            return self.getToken(SmallerBasicParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(SmallerBasicParser.MINUS, 0)

        def getRuleIndex(self):
            return SmallerBasicParser.RULE_unaryAtomNumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryAtomNumber" ):
                listener.enterUnaryAtomNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryAtomNumber" ):
                listener.exitUnaryAtomNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryAtomNumber" ):
                return visitor.visitUnaryAtomNumber(self)
            else:
                return visitor.visitChildren(self)




    def unaryAtomNumber(self):

        localctx = SmallerBasicParser.UnaryAtomNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_unaryAtomNumber)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==11:
                self.state = 271
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 274
            self.atomNumber()
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


        def getRuleIndex(self):
            return SmallerBasicParser.RULE_atomNumber

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AtomNumberIdContext(AtomNumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomNumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SmallerBasicParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomNumberId" ):
                listener.enterAtomNumberId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomNumberId" ):
                listener.exitAtomNumberId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomNumberId" ):
                return visitor.visitAtomNumberId(self)
            else:
                return visitor.visitChildren(self)


    class AtomNumberLibraryStatementContext(AtomNumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomNumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def libraryStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.LibraryStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomNumberLibraryStatement" ):
                listener.enterAtomNumberLibraryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomNumberLibraryStatement" ):
                listener.exitAtomNumberLibraryStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomNumberLibraryStatement" ):
                return visitor.visitAtomNumberLibraryStatement(self)
            else:
                return visitor.visitChildren(self)


    class AtomNumberParenthesisContext(AtomNumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomNumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LROUND(self):
            return self.getToken(SmallerBasicParser.LROUND, 0)
        def additiveExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.AdditiveExpressionContext,0)

        def RROUND(self):
            return self.getToken(SmallerBasicParser.RROUND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomNumberParenthesis" ):
                listener.enterAtomNumberParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomNumberParenthesis" ):
                listener.exitAtomNumberParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomNumberParenthesis" ):
                return visitor.visitAtomNumberParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class AtomNumberArrayAccessContext(AtomNumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomNumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arrayAccess(self):
            return self.getTypedRuleContext(SmallerBasicParser.ArrayAccessContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomNumberArrayAccess" ):
                listener.enterAtomNumberArrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomNumberArrayAccess" ):
                listener.exitAtomNumberArrayAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomNumberArrayAccess" ):
                return visitor.visitAtomNumberArrayAccess(self)
            else:
                return visitor.visitChildren(self)


    class AtomNumberFloatContext(AtomNumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomNumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(SmallerBasicParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomNumberFloat" ):
                listener.enterAtomNumberFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomNumberFloat" ):
                listener.exitAtomNumberFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomNumberFloat" ):
                return visitor.visitAtomNumberFloat(self)
            else:
                return visitor.visitChildren(self)


    class AtomNumberIntContext(AtomNumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomNumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SmallerBasicParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomNumberInt" ):
                listener.enterAtomNumberInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomNumberInt" ):
                listener.exitAtomNumberInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomNumberInt" ):
                return visitor.visitAtomNumberInt(self)
            else:
                return visitor.visitChildren(self)



    def atomNumber(self):

        localctx = SmallerBasicParser.AtomNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_atomNumber)
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.AtomNumberIntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.match(SmallerBasicParser.INT)
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.AtomNumberFloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(SmallerBasicParser.FLOAT)
                pass

            elif la_ == 3:
                localctx = SmallerBasicParser.AtomNumberIdContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 278
                self.match(SmallerBasicParser.ID)
                pass

            elif la_ == 4:
                localctx = SmallerBasicParser.AtomNumberParenthesisContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 279
                self.match(SmallerBasicParser.LROUND)
                self.state = 280
                self.additiveExpression()
                self.state = 281
                self.match(SmallerBasicParser.RROUND)
                pass

            elif la_ == 5:
                localctx = SmallerBasicParser.AtomNumberLibraryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 283
                self.libraryStatement()
                pass

            elif la_ == 6:
                localctx = SmallerBasicParser.AtomNumberArrayAccessContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 284
                self.arrayAccess()
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
        self.enterRule(localctx, 42, self.RULE_stringExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
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
        self.enterRule(localctx, 44, self.RULE_additiveStringExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.atomString()
            self.state = 294
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 290
                    self.match(SmallerBasicParser.PLUS)
                    self.state = 291
                    self.additiveStringExpression() 
                self.state = 296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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


    class AtomStringParenthesisContext(AtomStringContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomStringContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LROUND(self):
            return self.getToken(SmallerBasicParser.LROUND, 0)
        def stringExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.StringExpressionContext,0)

        def RROUND(self):
            return self.getToken(SmallerBasicParser.RROUND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomStringParenthesis" ):
                listener.enterAtomStringParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomStringParenthesis" ):
                listener.exitAtomStringParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomStringParenthesis" ):
                return visitor.visitAtomStringParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class AtomStringLiteralContext(AtomStringContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomStringContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(SmallerBasicParser.STRING, 0)

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


    class AtomStringArrayAccessContext(AtomStringContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SmallerBasicParser.AtomStringContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arrayAccess(self):
            return self.getTypedRuleContext(SmallerBasicParser.ArrayAccessContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomStringArrayAccess" ):
                listener.enterAtomStringArrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomStringArrayAccess" ):
                listener.exitAtomStringArrayAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomStringArrayAccess" ):
                return visitor.visitAtomStringArrayAccess(self)
            else:
                return visitor.visitChildren(self)



    def atomString(self):

        localctx = SmallerBasicParser.AtomStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_atomString)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.AtomStringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.match(SmallerBasicParser.STRING)
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.AtomStringIdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.match(SmallerBasicParser.ID)
                pass

            elif la_ == 3:
                localctx = SmallerBasicParser.AtomStringParenthesisContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 299
                self.match(SmallerBasicParser.LROUND)
                self.state = 300
                self.stringExpression()
                self.state = 301
                self.match(SmallerBasicParser.RROUND)
                pass

            elif la_ == 4:
                localctx = SmallerBasicParser.AtomStringLibraryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 303
                self.libraryStatement()
                pass

            elif la_ == 5:
                localctx = SmallerBasicParser.AtomStringArrayAccessContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 304
                self.arrayAccess()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





