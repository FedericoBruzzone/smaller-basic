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
        4,1,39,299,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,4,0,56,8,0,11,0,12,0,57,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,71,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,81,8,2,11,
        2,12,2,82,1,2,1,2,1,2,3,2,88,8,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,5,1,5,4,5,102,8,5,11,5,12,5,103,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,4,5,114,8,5,11,5,12,5,115,1,5,1,5,4,5,120,8,5,11,5,12,
        5,121,1,5,1,5,3,5,126,8,5,1,6,1,6,1,6,1,6,1,6,4,6,133,8,6,11,6,12,
        6,134,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,4,7,146,8,7,11,7,12,7,
        147,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,4,7,161,8,7,11,7,
        12,7,162,1,7,1,7,3,7,167,8,7,1,8,1,8,1,8,4,8,172,8,8,11,8,12,8,173,
        1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,4,10,185,8,10,11,10,12,10,
        186,1,10,1,10,3,10,191,8,10,1,10,1,10,1,11,1,11,1,11,1,11,3,11,199,
        8,11,1,12,1,12,1,12,4,12,204,8,12,11,12,12,12,205,1,12,3,12,209,
        8,12,1,13,1,13,1,13,1,13,1,13,3,13,216,8,13,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,3,14,225,8,14,1,15,1,15,1,16,1,16,1,16,4,16,232,8,
        16,11,16,12,16,233,1,16,3,16,237,8,16,1,17,1,17,1,17,4,17,242,8,
        17,11,17,12,17,243,1,17,3,17,247,8,17,1,18,1,18,1,18,3,18,252,8,
        18,1,18,1,18,1,18,1,18,1,18,3,18,259,8,18,1,18,3,18,262,8,18,1,19,
        1,19,1,20,1,20,1,20,5,20,269,8,20,10,20,12,20,272,9,20,1,21,1,21,
        1,21,3,21,277,8,21,1,22,1,22,1,22,1,22,3,22,283,8,22,1,23,3,23,286,
        8,23,1,23,1,23,1,24,1,24,1,25,1,25,1,26,3,26,295,8,26,1,26,1,26,
        1,26,0,0,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,0,4,1,0,20,21,1,0,14,19,1,0,10,11,1,0,12,
        13,319,0,55,1,0,0,0,2,70,1,0,0,0,4,87,1,0,0,0,6,89,1,0,0,0,8,92,
        1,0,0,0,10,125,1,0,0,0,12,127,1,0,0,0,14,166,1,0,0,0,16,168,1,0,
        0,0,18,177,1,0,0,0,20,181,1,0,0,0,22,198,1,0,0,0,24,208,1,0,0,0,
        26,215,1,0,0,0,28,224,1,0,0,0,30,226,1,0,0,0,32,236,1,0,0,0,34,246,
        1,0,0,0,36,261,1,0,0,0,38,263,1,0,0,0,40,265,1,0,0,0,42,276,1,0,
        0,0,44,282,1,0,0,0,46,285,1,0,0,0,48,289,1,0,0,0,50,291,1,0,0,0,
        52,294,1,0,0,0,54,56,3,2,1,0,55,54,1,0,0,0,56,57,1,0,0,0,57,55,1,
        0,0,0,57,58,1,0,0,0,58,59,1,0,0,0,59,60,5,0,0,1,60,1,1,0,0,0,61,
        71,3,4,2,0,62,71,3,12,6,0,63,71,3,14,7,0,64,71,3,10,5,0,65,71,3,
        6,3,0,66,71,3,8,4,0,67,71,3,16,8,0,68,71,3,18,9,0,69,71,3,20,10,
        0,70,61,1,0,0,0,70,62,1,0,0,0,70,63,1,0,0,0,70,64,1,0,0,0,70,65,
        1,0,0,0,70,66,1,0,0,0,70,67,1,0,0,0,70,68,1,0,0,0,70,69,1,0,0,0,
        71,3,1,0,0,0,72,73,5,35,0,0,73,74,5,16,0,0,74,88,3,22,11,0,75,80,
        5,35,0,0,76,77,5,6,0,0,77,78,3,30,15,0,78,79,5,7,0,0,79,81,1,0,0,
        0,80,76,1,0,0,0,81,82,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,84,
        1,0,0,0,84,85,5,16,0,0,85,86,3,22,11,0,86,88,1,0,0,0,87,72,1,0,0,
        0,87,75,1,0,0,0,88,5,1,0,0,0,89,90,5,35,0,0,90,91,5,9,0,0,91,7,1,
        0,0,0,92,93,5,32,0,0,93,94,5,35,0,0,94,9,1,0,0,0,95,96,5,22,0,0,
        96,97,5,4,0,0,97,98,3,24,12,0,98,99,5,5,0,0,99,101,5,23,0,0,100,
        102,3,2,1,0,101,100,1,0,0,0,102,103,1,0,0,0,103,101,1,0,0,0,103,
        104,1,0,0,0,104,105,1,0,0,0,105,106,5,25,0,0,106,126,1,0,0,0,107,
        108,5,22,0,0,108,109,5,4,0,0,109,110,3,24,12,0,110,111,5,5,0,0,111,
        113,5,23,0,0,112,114,3,2,1,0,113,112,1,0,0,0,114,115,1,0,0,0,115,
        113,1,0,0,0,115,116,1,0,0,0,116,117,1,0,0,0,117,119,5,24,0,0,118,
        120,3,2,1,0,119,118,1,0,0,0,120,121,1,0,0,0,121,119,1,0,0,0,121,
        122,1,0,0,0,122,123,1,0,0,0,123,124,5,25,0,0,124,126,1,0,0,0,125,
        95,1,0,0,0,125,107,1,0,0,0,126,11,1,0,0,0,127,128,5,26,0,0,128,129,
        5,4,0,0,129,130,3,24,12,0,130,132,5,5,0,0,131,133,3,2,1,0,132,131,
        1,0,0,0,133,134,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,136,
        1,0,0,0,136,137,5,27,0,0,137,13,1,0,0,0,138,139,5,28,0,0,139,140,
        5,35,0,0,140,141,5,16,0,0,141,142,3,30,15,0,142,143,5,29,0,0,143,
        145,3,30,15,0,144,146,3,2,1,0,145,144,1,0,0,0,146,147,1,0,0,0,147,
        145,1,0,0,0,147,148,1,0,0,0,148,149,1,0,0,0,149,150,5,31,0,0,150,
        167,1,0,0,0,151,152,5,28,0,0,152,153,5,35,0,0,153,154,5,16,0,0,154,
        155,3,30,15,0,155,156,5,29,0,0,156,157,3,30,15,0,157,158,5,30,0,
        0,158,160,3,30,15,0,159,161,3,2,1,0,160,159,1,0,0,0,161,162,1,0,
        0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,165,5,31,
        0,0,165,167,1,0,0,0,166,138,1,0,0,0,166,151,1,0,0,0,167,15,1,0,0,
        0,168,169,5,33,0,0,169,171,5,35,0,0,170,172,3,2,1,0,171,170,1,0,
        0,0,172,173,1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,175,1,0,
        0,0,175,176,5,34,0,0,176,17,1,0,0,0,177,178,5,35,0,0,178,179,5,4,
        0,0,179,180,5,5,0,0,180,19,1,0,0,0,181,184,5,35,0,0,182,183,5,8,
        0,0,183,185,5,35,0,0,184,182,1,0,0,0,185,186,1,0,0,0,186,184,1,0,
        0,0,186,187,1,0,0,0,187,188,1,0,0,0,188,190,5,4,0,0,189,191,3,22,
        11,0,190,189,1,0,0,0,190,191,1,0,0,0,191,192,1,0,0,0,192,193,5,5,
        0,0,193,21,1,0,0,0,194,199,3,24,12,0,195,199,3,30,15,0,196,199,3,
        38,19,0,197,199,3,44,22,0,198,194,1,0,0,0,198,195,1,0,0,0,198,196,
        1,0,0,0,198,197,1,0,0,0,199,23,1,0,0,0,200,203,3,26,13,0,201,202,
        7,0,0,0,202,204,3,26,13,0,203,201,1,0,0,0,204,205,1,0,0,0,205,203,
        1,0,0,0,205,206,1,0,0,0,206,209,1,0,0,0,207,209,3,26,13,0,208,200,
        1,0,0,0,208,207,1,0,0,0,209,25,1,0,0,0,210,211,3,30,15,0,211,212,
        7,1,0,0,212,213,3,30,15,0,213,216,1,0,0,0,214,216,3,28,14,0,215,
        210,1,0,0,0,215,214,1,0,0,0,216,27,1,0,0,0,217,225,3,50,25,0,218,
        225,3,52,26,0,219,220,5,4,0,0,220,221,3,24,12,0,221,222,5,5,0,0,
        222,225,1,0,0,0,223,225,3,20,10,0,224,217,1,0,0,0,224,218,1,0,0,
        0,224,219,1,0,0,0,224,223,1,0,0,0,225,29,1,0,0,0,226,227,3,32,16,
        0,227,31,1,0,0,0,228,231,3,34,17,0,229,230,7,2,0,0,230,232,3,34,
        17,0,231,229,1,0,0,0,232,233,1,0,0,0,233,231,1,0,0,0,233,234,1,0,
        0,0,234,237,1,0,0,0,235,237,3,34,17,0,236,228,1,0,0,0,236,235,1,
        0,0,0,237,33,1,0,0,0,238,241,3,36,18,0,239,240,7,3,0,0,240,242,3,
        36,18,0,241,239,1,0,0,0,242,243,1,0,0,0,243,241,1,0,0,0,243,244,
        1,0,0,0,244,247,1,0,0,0,245,247,3,36,18,0,246,238,1,0,0,0,246,245,
        1,0,0,0,247,35,1,0,0,0,248,262,3,46,23,0,249,262,3,52,26,0,250,252,
        5,11,0,0,251,250,1,0,0,0,251,252,1,0,0,0,252,253,1,0,0,0,253,254,
        5,4,0,0,254,255,3,30,15,0,255,256,5,5,0,0,256,262,1,0,0,0,257,259,
        5,11,0,0,258,257,1,0,0,0,258,259,1,0,0,0,259,260,1,0,0,0,260,262,
        3,20,10,0,261,248,1,0,0,0,261,249,1,0,0,0,261,251,1,0,0,0,261,258,
        1,0,0,0,262,37,1,0,0,0,263,264,3,40,20,0,264,39,1,0,0,0,265,270,
        3,42,21,0,266,267,5,10,0,0,267,269,3,42,21,0,268,266,1,0,0,0,269,
        272,1,0,0,0,270,268,1,0,0,0,270,271,1,0,0,0,271,41,1,0,0,0,272,270,
        1,0,0,0,273,277,3,48,24,0,274,277,3,52,26,0,275,277,3,20,10,0,276,
        273,1,0,0,0,276,274,1,0,0,0,276,275,1,0,0,0,277,43,1,0,0,0,278,283,
        3,46,23,0,279,283,3,48,24,0,280,283,3,50,25,0,281,283,3,52,26,0,
        282,278,1,0,0,0,282,279,1,0,0,0,282,280,1,0,0,0,282,281,1,0,0,0,
        283,45,1,0,0,0,284,286,7,2,0,0,285,284,1,0,0,0,285,286,1,0,0,0,286,
        287,1,0,0,0,287,288,5,1,0,0,288,47,1,0,0,0,289,290,5,2,0,0,290,49,
        1,0,0,0,291,292,5,3,0,0,292,51,1,0,0,0,293,295,7,2,0,0,294,293,1,
        0,0,0,294,295,1,0,0,0,295,296,1,0,0,0,296,297,5,35,0,0,297,53,1,
        0,0,0,32,57,70,82,87,103,115,121,125,134,147,162,166,173,186,190,
        198,205,208,215,224,233,236,243,246,251,258,261,270,276,282,285,
        294
    ]

class SmallerBasicParser ( Parser ):

    grammarFileName = "SmallerBasic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "'.'", "':'", "'+'", "'-'", 
                     "'*'", "'/'", "'>'", "'<'", "'='", "'>='", "'<='", 
                     "'<>'", "'And'", "'Or'", "'If'", "'Then'", "'Else'", 
                     "'EndIf'", "'While'", "'EndWhile'", "'For'", "'To'", 
                     "'Step'", "'EndFor'", "'Goto'", "'Sub'", "'EndSub'" ]

    symbolicNames = [ "<INVALID>", "NUMBER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "LROUND", "RROUND", "LSQUARE", "RSQUARE", "DOT", "COLON", 
                      "PLUS", "MINUS", "MUL", "DIV", "GT", "LT", "EQ", "GTEQ", 
                      "LTEQ", "NEQ", "AND", "OR", "IF", "THEN", "ELSE", 
                      "ENDIF", "WHILE", "ENDWHILE", "FOR", "TO", "STEP", 
                      "ENDFOR", "GOTO", "SUB", "ENDSUB", "ID", "WS", "COMMENT", 
                      "NEWLINE", "LINE_COMMENT" ]

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
    RULE_signedNumber = 23
    RULE_string = 24
    RULE_boolean = 25
    RULE_id = 26

    ruleNames =  [ "program", "statement", "declarationStatement", "labelStatement", 
                   "gotoStatement", "ifStatement", "whileStatement", "forStatement", 
                   "subroutineStatement", "callSubroutineStatement", "libraryStatement", 
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
    DOT=8
    COLON=9
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
    WS=36
    COMMENT=37
    NEWLINE=38
    LINE_COMMENT=39

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
            self.state = 55 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self.statement()
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0)):
                    break

            self.state = 59
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
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.declarationStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.whileStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.forStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 65
                self.labelStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 66
                self.gotoStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 67
                self.subroutineStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 68
                self.callSubroutineStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 69
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
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(SmallerBasicParser.ID)
                self.state = 73
                self.match(SmallerBasicParser.EQ)
                self.state = 74
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(SmallerBasicParser.ID)
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 76
                    self.match(SmallerBasicParser.LSQUARE)
                    self.state = 77
                    self.arithmeticalExpression()
                    self.state = 78
                    self.match(SmallerBasicParser.RSQUARE)
                    self.state = 82 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==6):
                        break

                self.state = 84
                self.match(SmallerBasicParser.EQ)
                self.state = 85
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
            self.state = 89
            self.match(SmallerBasicParser.ID)
            self.state = 90
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
            self.state = 92
            self.match(SmallerBasicParser.GOTO)
            self.state = 93
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
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(SmallerBasicParser.IF)
                self.state = 96
                self.match(SmallerBasicParser.LROUND)
                self.state = 97
                self.logicalExpression()
                self.state = 98
                self.match(SmallerBasicParser.RROUND)
                self.state = 99
                self.match(SmallerBasicParser.THEN)
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 100
                    self.statement()
                    self.state = 103 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0)):
                        break

                self.state = 105
                self.match(SmallerBasicParser.ENDIF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(SmallerBasicParser.IF)
                self.state = 108
                self.match(SmallerBasicParser.LROUND)
                self.state = 109
                self.logicalExpression()
                self.state = 110
                self.match(SmallerBasicParser.RROUND)
                self.state = 111
                self.match(SmallerBasicParser.THEN)
                self.state = 113 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 112
                    self.statement()
                    self.state = 115 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0)):
                        break

                self.state = 117
                self.match(SmallerBasicParser.ELSE)
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 118
                    self.statement()
                    self.state = 121 
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
            self.state = 127
            self.match(SmallerBasicParser.WHILE)
            self.state = 128
            self.match(SmallerBasicParser.LROUND)
            self.state = 129
            self.logicalExpression()
            self.state = 130
            self.match(SmallerBasicParser.RROUND)
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

            self.state = 136
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
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(SmallerBasicParser.FOR)
                self.state = 139
                self.match(SmallerBasicParser.ID)
                self.state = 140
                self.match(SmallerBasicParser.EQ)
                self.state = 141
                self.arithmeticalExpression()
                self.state = 142
                self.match(SmallerBasicParser.TO)
                self.state = 143
                self.arithmeticalExpression()
                self.state = 145 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 144
                    self.statement()
                    self.state = 147 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0)):
                        break

                self.state = 149
                self.match(SmallerBasicParser.ENDFOR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(SmallerBasicParser.FOR)
                self.state = 152
                self.match(SmallerBasicParser.ID)
                self.state = 153
                self.match(SmallerBasicParser.EQ)
                self.state = 154
                self.arithmeticalExpression()
                self.state = 155
                self.match(SmallerBasicParser.TO)
                self.state = 156
                self.arithmeticalExpression()
                self.state = 157
                self.match(SmallerBasicParser.STEP)
                self.state = 158
                self.arithmeticalExpression()
                self.state = 160 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 159
                    self.statement()
                    self.state = 162 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0)):
                        break

                self.state = 164
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
            self.state = 168
            self.match(SmallerBasicParser.SUB)
            self.state = 169
            self.match(SmallerBasicParser.ID)
            self.state = 171 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 170
                self.statement()
                self.state = 173 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 47584378880) != 0)):
                    break

            self.state = 175
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
            self.state = 177
            self.match(SmallerBasicParser.ID)
            self.state = 178
            self.match(SmallerBasicParser.LROUND)
            self.state = 179
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
            self.state = 181
            self.match(SmallerBasicParser.ID)
            self.state = 184 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 182
                self.match(SmallerBasicParser.DOT)
                self.state = 183
                self.match(SmallerBasicParser.ID)
                self.state = 186 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8):
                    break

            self.state = 188
            self.match(SmallerBasicParser.LROUND)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34359741470) != 0):
                self.state = 189
                self.expression()


            self.state = 192
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

        def logicalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.LogicalExpressionContext,0)


        def arithmeticalExpression(self):
            return self.getTypedRuleContext(SmallerBasicParser.ArithmeticalExpressionContext,0)


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
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.logicalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.arithmeticalExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                self.stringExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 197
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
        self.enterRule(localctx, 24, self.RULE_logicalExpression)
        self._la = 0 # Token type
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.booleanExpression()
                self.state = 203 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 201
                    _la = self._input.LA(1)
                    if not(_la==20 or _la==21):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 202
                    self.booleanExpression()
                    self.state = 205 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==20 or _la==21):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
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
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.arithmeticalExpression()
                self.state = 211
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 212
                self.arithmeticalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
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

        def libraryStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.LibraryStatementContext,0)


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
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.boolean()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.id_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 219
                self.match(SmallerBasicParser.LROUND)
                self.state = 220
                self.logicalExpression()
                self.state = 221
                self.match(SmallerBasicParser.RROUND)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 223
                self.libraryStatement()
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
            self.state = 226
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
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.multiplicativeExpression()
                self.state = 231 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 229
                    _la = self._input.LA(1)
                    if not(_la==10 or _la==11):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 230
                    self.multiplicativeExpression()
                    self.state = 233 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==10 or _la==11):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
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
        self.enterRule(localctx, 34, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.atomNumber()
                self.state = 241 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 239
                    _la = self._input.LA(1)
                    if not(_la==12 or _la==13):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 240
                    self.atomNumber()
                    self.state = 243 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==12 or _la==13):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
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
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.signedNumber()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.id_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 250
                    self.match(SmallerBasicParser.MINUS)


                self.state = 253
                self.match(SmallerBasicParser.LROUND)
                self.state = 254
                self.arithmeticalExpression()
                self.state = 255
                self.match(SmallerBasicParser.RROUND)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 257
                    self.match(SmallerBasicParser.MINUS)


                self.state = 260
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
            self.state = 263
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
        self.enterRule(localctx, 40, self.RULE_additiveStringExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.atomString()
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 266
                self.match(SmallerBasicParser.PLUS)
                self.state = 267
                self.atomString()
                self.state = 272
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


        def libraryStatement(self):
            return self.getTypedRuleContext(SmallerBasicParser.LibraryStatementContext,0)


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
        self.enterRule(localctx, 42, self.RULE_atomString)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.string()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.id_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
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
        self.enterRule(localctx, 44, self.RULE_literal)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.signedNumber()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.string()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
                self.boolean()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 281
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
        self.enterRule(localctx, 46, self.RULE_signedNumber)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==11:
                self.state = 284
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 287
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
        self.enterRule(localctx, 48, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
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
        self.enterRule(localctx, 50, self.RULE_boolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
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
        self.enterRule(localctx, 52, self.RULE_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==11:
                self.state = 293
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 296
            self.match(SmallerBasicParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





