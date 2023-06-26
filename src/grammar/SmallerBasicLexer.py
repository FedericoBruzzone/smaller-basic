# Generated from src/grammar/SmallerBasic.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,45,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,5,3,27,8,3,10,
        3,12,3,30,9,3,1,4,4,4,33,8,4,11,4,12,4,34,1,5,1,5,1,6,4,6,40,8,6,
        11,6,12,6,41,1,6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,3,1,
        0,48,57,2,0,65,90,97,122,3,0,9,10,13,13,32,32,48,0,1,1,0,0,0,0,3,
        1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,
        0,0,0,1,15,1,0,0,0,3,19,1,0,0,0,5,21,1,0,0,0,7,23,1,0,0,0,9,32,1,
        0,0,0,11,36,1,0,0,0,13,39,1,0,0,0,15,16,5,118,0,0,16,17,5,97,0,0,
        17,18,5,114,0,0,18,2,1,0,0,0,19,20,5,61,0,0,20,4,1,0,0,0,21,22,5,
        59,0,0,22,6,1,0,0,0,23,28,3,11,5,0,24,27,3,11,5,0,25,27,7,0,0,0,
        26,24,1,0,0,0,26,25,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,28,29,1,
        0,0,0,29,8,1,0,0,0,30,28,1,0,0,0,31,33,7,0,0,0,32,31,1,0,0,0,33,
        34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,10,1,0,0,0,36,37,7,1,0,
        0,37,12,1,0,0,0,38,40,7,2,0,0,39,38,1,0,0,0,40,41,1,0,0,0,41,39,
        1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,43,44,6,6,0,0,44,14,1,0,0,0,
        5,0,26,28,34,41,1,6,0,0
    ]

class SmallerBasicLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    ID = 4
    INT = 5
    LETTER = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'var'", "'='", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "LETTER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "ID", "INT", "LETTER", "WS" ]

    grammarFileName = "SmallerBasic.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


