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
        4,1,40,273,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,4,0,48,8,0,11,0,12,0,49,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,63,8,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,4,2,73,8,2,11,2,12,2,74,1,2,1,2,1,2,3,2,80,8,2,1,3,1,3,
        1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,4,5,94,8,5,11,5,12,5,95,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,4,5,106,8,5,11,5,12,5,107,1,5,1,
        5,4,5,112,8,5,11,5,12,5,113,1,5,1,5,3,5,118,8,5,1,6,1,6,1,6,1,6,
        1,6,4,6,125,8,6,11,6,12,6,126,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,4,7,138,8,7,11,7,12,7,139,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,4,7,153,8,7,11,7,12,7,154,1,7,1,7,3,7,159,8,7,1,8,1,8,1,
        8,4,8,164,8,8,11,8,12,8,165,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,186,8,10,1,
        11,1,11,1,11,3,11,191,8,11,1,12,1,12,1,12,5,12,196,8,12,10,12,12,
        12,199,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,210,
        8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,219,8,14,1,15,1,15,
        1,16,1,16,1,16,5,16,226,8,16,10,16,12,16,229,9,16,1,17,1,17,1,17,
        5,17,234,8,17,10,17,12,17,237,9,17,1,18,3,18,240,8,18,1,18,1,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,252,8,19,1,20,1,20,
        1,21,1,21,1,21,5,21,259,8,21,10,21,12,21,262,9,21,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,3,22,271,8,22,1,22,0,0,23,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,4,1,0,19,20,1,0,13,
        18,1,0,9,10,1,0,11,12,289,0,47,1,0,0,0,2,62,1,0,0,0,4,79,1,0,0,0,
        6,81,1,0,0,0,8,84,1,0,0,0,10,117,1,0,0,0,12,119,1,0,0,0,14,158,1,
        0,0,0,16,160,1,0,0,0,18,169,1,0,0,0,20,185,1,0,0,0,22,190,1,0,0,
        0,24,192,1,0,0,0,26,209,1,0,0,0,28,218,1,0,0,0,30,220,1,0,0,0,32,
        222,1,0,0,0,34,230,1,0,0,0,36,239,1,0,0,0,38,251,1,0,0,0,40,253,
        1,0,0,0,42,255,1,0,0,0,44,270,1,0,0,0,46,48,3,2,1,0,47,46,1,0,0,
        0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,51,52,
        5,0,0,1,52,1,1,0,0,0,53,63,3,4,2,0,54,63,3,12,6,0,55,63,3,14,7,0,
        56,63,3,10,5,0,57,63,3,6,3,0,58,63,3,8,4,0,59,63,3,16,8,0,60,63,
        3,18,9,0,61,63,3,20,10,0,62,53,1,0,0,0,62,54,1,0,0,0,62,55,1,0,0,
        0,62,56,1,0,0,0,62,57,1,0,0,0,62,58,1,0,0,0,62,59,1,0,0,0,62,60,
        1,0,0,0,62,61,1,0,0,0,63,3,1,0,0,0,64,65,5,34,0,0,65,66,5,15,0,0,
        66,80,3,22,11,0,67,72,5,34,0,0,68,69,5,5,0,0,69,70,3,30,15,0,70,
        71,5,6,0,0,71,73,1,0,0,0,72,68,1,0,0,0,73,74,1,0,0,0,74,72,1,0,0,
        0,74,75,1,0,0,0,75,76,1,0,0,0,76,77,5,15,0,0,77,78,3,22,11,0,78,
        80,1,0,0,0,79,64,1,0,0,0,79,67,1,0,0,0,80,5,1,0,0,0,81,82,5,34,0,
        0,82,83,5,8,0,0,83,7,1,0,0,0,84,85,5,31,0,0,85,86,5,34,0,0,86,9,
        1,0,0,0,87,88,5,21,0,0,88,89,5,3,0,0,89,90,3,24,12,0,90,91,5,4,0,
        0,91,93,5,22,0,0,92,94,3,2,1,0,93,92,1,0,0,0,94,95,1,0,0,0,95,93,
        1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,0,97,98,5,24,0,0,98,118,1,0,0,
        0,99,100,5,21,0,0,100,101,5,3,0,0,101,102,3,24,12,0,102,103,5,4,
        0,0,103,105,5,22,0,0,104,106,3,2,1,0,105,104,1,0,0,0,106,107,1,0,
        0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,109,1,0,0,0,109,111,5,23,
        0,0,110,112,3,2,1,0,111,110,1,0,0,0,112,113,1,0,0,0,113,111,1,0,
        0,0,113,114,1,0,0,0,114,115,1,0,0,0,115,116,5,24,0,0,116,118,1,0,
        0,0,117,87,1,0,0,0,117,99,1,0,0,0,118,11,1,0,0,0,119,120,5,25,0,
        0,120,121,5,3,0,0,121,122,3,24,12,0,122,124,5,4,0,0,123,125,3,2,
        1,0,124,123,1,0,0,0,125,126,1,0,0,0,126,124,1,0,0,0,126,127,1,0,
        0,0,127,128,1,0,0,0,128,129,5,26,0,0,129,13,1,0,0,0,130,131,5,27,
        0,0,131,132,5,34,0,0,132,133,5,15,0,0,133,134,3,30,15,0,134,135,
        5,28,0,0,135,137,3,30,15,0,136,138,3,2,1,0,137,136,1,0,0,0,138,139,
        1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,142,
        5,30,0,0,142,159,1,0,0,0,143,144,5,27,0,0,144,145,5,34,0,0,145,146,
        5,15,0,0,146,147,3,30,15,0,147,148,5,28,0,0,148,149,3,30,15,0,149,
        150,5,29,0,0,150,152,3,30,15,0,151,153,3,2,1,0,152,151,1,0,0,0,153,
        154,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,156,1,0,0,0,156,
        157,5,30,0,0,157,159,1,0,0,0,158,130,1,0,0,0,158,143,1,0,0,0,159,
        15,1,0,0,0,160,161,5,32,0,0,161,163,5,34,0,0,162,164,3,2,1,0,163,
        162,1,0,0,0,164,165,1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,0,166,
        167,1,0,0,0,167,168,5,33,0,0,168,17,1,0,0,0,169,170,5,34,0,0,170,
        171,5,3,0,0,171,172,5,4,0,0,172,19,1,0,0,0,173,174,5,34,0,0,174,
        175,5,7,0,0,175,176,5,34,0,0,176,177,5,3,0,0,177,178,3,22,11,0,178,
        179,5,4,0,0,179,186,1,0,0,0,180,181,5,34,0,0,181,182,5,7,0,0,182,
        183,5,34,0,0,183,184,5,3,0,0,184,186,5,4,0,0,185,173,1,0,0,0,185,
        180,1,0,0,0,186,21,1,0,0,0,187,191,3,24,12,0,188,191,3,30,15,0,189,
        191,3,40,20,0,190,187,1,0,0,0,190,188,1,0,0,0,190,189,1,0,0,0,191,
        23,1,0,0,0,192,197,3,26,13,0,193,194,7,0,0,0,194,196,3,26,13,0,195,
        193,1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,
        25,1,0,0,0,199,197,1,0,0,0,200,201,3,30,15,0,201,202,7,1,0,0,202,
        203,3,30,15,0,203,210,1,0,0,0,204,205,3,40,20,0,205,206,7,1,0,0,
        206,207,3,40,20,0,207,210,1,0,0,0,208,210,3,28,14,0,209,200,1,0,
        0,0,209,204,1,0,0,0,209,208,1,0,0,0,210,27,1,0,0,0,211,219,5,2,0,
        0,212,219,5,34,0,0,213,214,5,3,0,0,214,215,3,24,12,0,215,216,5,4,
        0,0,216,219,1,0,0,0,217,219,3,20,10,0,218,211,1,0,0,0,218,212,1,
        0,0,0,218,213,1,0,0,0,218,217,1,0,0,0,219,29,1,0,0,0,220,221,3,32,
        16,0,221,31,1,0,0,0,222,227,3,34,17,0,223,224,7,2,0,0,224,226,3,
        34,17,0,225,223,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,228,
        1,0,0,0,228,33,1,0,0,0,229,227,1,0,0,0,230,235,3,36,18,0,231,232,
        7,3,0,0,232,234,3,34,17,0,233,231,1,0,0,0,234,237,1,0,0,0,235,233,
        1,0,0,0,235,236,1,0,0,0,236,35,1,0,0,0,237,235,1,0,0,0,238,240,7,
        2,0,0,239,238,1,0,0,0,239,240,1,0,0,0,240,241,1,0,0,0,241,242,3,
        38,19,0,242,37,1,0,0,0,243,252,5,35,0,0,244,252,5,36,0,0,245,252,
        5,34,0,0,246,247,5,3,0,0,247,248,3,32,16,0,248,249,5,4,0,0,249,252,
        1,0,0,0,250,252,3,20,10,0,251,243,1,0,0,0,251,244,1,0,0,0,251,245,
        1,0,0,0,251,246,1,0,0,0,251,250,1,0,0,0,252,39,1,0,0,0,253,254,3,
        42,21,0,254,41,1,0,0,0,255,260,3,44,22,0,256,257,5,9,0,0,257,259,
        3,42,21,0,258,256,1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,260,261,
        1,0,0,0,261,43,1,0,0,0,262,260,1,0,0,0,263,271,5,1,0,0,264,271,5,
        34,0,0,265,266,5,3,0,0,266,267,3,40,20,0,267,268,5,4,0,0,268,271,
        1,0,0,0,269,271,3,20,10,0,270,263,1,0,0,0,270,264,1,0,0,0,270,265,
        1,0,0,0,270,269,1,0,0,0,271,45,1,0,0,0,24,49,62,74,79,95,107,113,
        117,126,139,154,158,165,185,190,197,209,218,227,235,239,251,260,
        270
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

    symbolicNames = [ "<INVALID>", "STRING", "BOOLEAN", "LROUND", "RROUND", 
                      "LSQUARE", "RSQUARE", "DOT", "COLON", "PLUS", "MINUS", 
                      "MUL", "DIV", "GT", "LT", "EQ", "GTEQ", "LTEQ", "NEQ", 
                      "AND", "OR", "IF", "THEN", "ELSE", "ENDIF", "WHILE", 
                      "ENDWHILE", "FOR", "TO", "STEP", "ENDFOR", "GOTO", 
                      "SUB", "ENDSUB", "ID", "INT", "FLOAT", "WS", "COMMENT", 
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
    RULE_unaryAtomNumber = 18
    RULE_atomNumber = 19
    RULE_stringExpression = 20
    RULE_additiveStringExpression = 21
    RULE_atomString = 22

    ruleNames =  [ "program", "statement", "declarationStatement", "labelStatement", 
                   "gotoStatement", "ifStatement", "whileStatement", "forStatement", 
                   "subroutineStatement", "callSubroutineStatement", "libraryStatement", 
                   "expression", "logicalExpression", "booleanExpression", 
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
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.statement()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                    break

            self.state = 51
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
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.declarationStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.whileStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.forStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 57
                self.labelStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 58
                self.gotoStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 59
                self.subroutineStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 60
                self.callSubroutineStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 61
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
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.VariableDeclarationStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(SmallerBasicParser.ID)
                self.state = 65
                self.match(SmallerBasicParser.EQ)
                self.state = 66
                self.expression()
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.ArrayDeclarationStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(SmallerBasicParser.ID)
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 68
                    self.match(SmallerBasicParser.LSQUARE)
                    self.state = 69
                    self.arithmeticalExpression()
                    self.state = 70
                    self.match(SmallerBasicParser.RSQUARE)
                    self.state = 74 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==5):
                        break

                self.state = 76
                self.match(SmallerBasicParser.EQ)
                self.state = 77
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
            self.state = 81
            self.match(SmallerBasicParser.ID)
            self.state = 82
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
            self.state = 84
            self.match(SmallerBasicParser.GOTO)
            self.state = 85
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
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(SmallerBasicParser.IF)
                self.state = 88
                self.match(SmallerBasicParser.LROUND)
                self.state = 89
                self.logicalExpression()
                self.state = 90
                self.match(SmallerBasicParser.RROUND)
                self.state = 91
                self.match(SmallerBasicParser.THEN)
                self.state = 93 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 92
                    self.statement()
                    self.state = 95 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                        break

                self.state = 97
                self.match(SmallerBasicParser.ENDIF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.match(SmallerBasicParser.IF)
                self.state = 100
                self.match(SmallerBasicParser.LROUND)
                self.state = 101
                self.logicalExpression()
                self.state = 102
                self.match(SmallerBasicParser.RROUND)
                self.state = 103
                self.match(SmallerBasicParser.THEN)
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 104
                    self.statement()
                    self.state = 107 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                        break

                self.state = 109
                self.match(SmallerBasicParser.ELSE)
                self.state = 111 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 110
                    self.statement()
                    self.state = 113 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                        break

                self.state = 115
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
            self.state = 119
            self.match(SmallerBasicParser.WHILE)
            self.state = 120
            self.match(SmallerBasicParser.LROUND)
            self.state = 121
            self.logicalExpression()
            self.state = 122
            self.match(SmallerBasicParser.RROUND)
            self.state = 124 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 123
                self.statement()
                self.state = 126 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                    break

            self.state = 128
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
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(SmallerBasicParser.FOR)
                self.state = 131
                self.match(SmallerBasicParser.ID)
                self.state = 132
                self.match(SmallerBasicParser.EQ)
                self.state = 133
                self.arithmeticalExpression()
                self.state = 134
                self.match(SmallerBasicParser.TO)
                self.state = 135
                self.arithmeticalExpression()
                self.state = 137 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 136
                    self.statement()
                    self.state = 139 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                        break

                self.state = 141
                self.match(SmallerBasicParser.ENDFOR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(SmallerBasicParser.FOR)
                self.state = 144
                self.match(SmallerBasicParser.ID)
                self.state = 145
                self.match(SmallerBasicParser.EQ)
                self.state = 146
                self.arithmeticalExpression()
                self.state = 147
                self.match(SmallerBasicParser.TO)
                self.state = 148
                self.arithmeticalExpression()
                self.state = 149
                self.match(SmallerBasicParser.STEP)
                self.state = 150
                self.arithmeticalExpression()
                self.state = 152 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 151
                    self.statement()
                    self.state = 154 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                        break

                self.state = 156
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
            self.state = 160
            self.match(SmallerBasicParser.SUB)
            self.state = 161
            self.match(SmallerBasicParser.ID)
            self.state = 163 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 162
                self.statement()
                self.state = 165 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 23792189440) != 0)):
                    break

            self.state = 167
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
            self.state = 169
            self.match(SmallerBasicParser.ID)
            self.state = 170
            self.match(SmallerBasicParser.LROUND)
            self.state = 171
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
        def expression(self):
            return self.getTypedRuleContext(SmallerBasicParser.ExpressionContext,0)

        def RROUND(self):
            return self.getToken(SmallerBasicParser.RROUND, 0)

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
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.LibraryStatementWithParametersContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(SmallerBasicParser.ID)
                self.state = 174
                self.match(SmallerBasicParser.DOT)
                self.state = 175
                self.match(SmallerBasicParser.ID)
                self.state = 176
                self.match(SmallerBasicParser.LROUND)
                self.state = 177
                self.expression()
                self.state = 178
                self.match(SmallerBasicParser.RROUND)
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.LibraryStatementWithoutParametersContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.match(SmallerBasicParser.ID)
                self.state = 181
                self.match(SmallerBasicParser.DOT)
                self.state = 182
                self.match(SmallerBasicParser.ID)
                self.state = 183
                self.match(SmallerBasicParser.LROUND)
                self.state = 184
                self.match(SmallerBasicParser.RROUND)
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
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.logicalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.arithmeticalExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
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
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.booleanExpression()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==20:
                self.state = 193
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 194
                self.booleanExpression()
                self.state = 199
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
        self.enterRule(localctx, 26, self.RULE_booleanExpression)
        self._la = 0 # Token type
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.BooleanArithmeticalExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.arithmeticalExpression()
                self.state = 201
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 202
                self.arithmeticalExpression()
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.BooleanStringExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.stringExpression()
                self.state = 205
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 206
                self.stringExpression()
                pass

            elif la_ == 3:
                localctx = SmallerBasicParser.BooleanAtomExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 208
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



    def atomBoolean(self):

        localctx = SmallerBasicParser.AtomBooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_atomBoolean)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.AtomBooleanBooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(SmallerBasicParser.BOOLEAN)
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.AtomBooleanIdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(SmallerBasicParser.ID)
                pass

            elif la_ == 3:
                localctx = SmallerBasicParser.AtomBooleanParenthesisContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.match(SmallerBasicParser.LROUND)
                self.state = 214
                self.logicalExpression()
                self.state = 215
                self.match(SmallerBasicParser.RROUND)
                pass

            elif la_ == 4:
                localctx = SmallerBasicParser.AtomBooleanLibraryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 217
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
            self.state = 220
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
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.multiplicativeExpression()
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 223
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 224
                self.multiplicativeExpression()
                self.state = 229
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
        self.enterRule(localctx, 34, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.unaryAtomNumber()
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 231
                    _la = self._input.LA(1)
                    if not(_la==11 or _la==12):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 232
                    self.multiplicativeExpression() 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 36, self.RULE_unaryAtomNumber)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9 or _la==10:
                self.state = 238
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 241
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
        self.enterRule(localctx, 38, self.RULE_atomNumber)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.AtomNumberIntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(SmallerBasicParser.INT)
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.AtomNumberFloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(SmallerBasicParser.FLOAT)
                pass

            elif la_ == 3:
                localctx = SmallerBasicParser.AtomNumberIdContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 245
                self.match(SmallerBasicParser.ID)
                pass

            elif la_ == 4:
                localctx = SmallerBasicParser.AtomNumberParenthesisContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.match(SmallerBasicParser.LROUND)
                self.state = 247
                self.additiveExpression()
                self.state = 248
                self.match(SmallerBasicParser.RROUND)
                pass

            elif la_ == 5:
                localctx = SmallerBasicParser.AtomNumberLibraryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 250
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
        self.enterRule(localctx, 40, self.RULE_stringExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
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
        self.enterRule(localctx, 42, self.RULE_additiveStringExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.atomString()
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 256
                    self.match(SmallerBasicParser.PLUS)
                    self.state = 257
                    self.additiveStringExpression() 
                self.state = 262
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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



    def atomString(self):

        localctx = SmallerBasicParser.AtomStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_atomString)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = SmallerBasicParser.AtomStringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(SmallerBasicParser.STRING)
                pass

            elif la_ == 2:
                localctx = SmallerBasicParser.AtomStringIdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(SmallerBasicParser.ID)
                pass

            elif la_ == 3:
                localctx = SmallerBasicParser.AtomStringParenthesisContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.match(SmallerBasicParser.LROUND)
                self.state = 266
                self.stringExpression()
                self.state = 267
                self.match(SmallerBasicParser.RROUND)
                pass

            elif la_ == 4:
                localctx = SmallerBasicParser.AtomStringLibraryStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 269
                self.libraryStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





