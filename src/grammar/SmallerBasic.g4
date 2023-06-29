// SmallerBasic grammar for ANTLR4
grammar SmallerBasic;

program
    : statement+ EOF
    ;

expression
    : NUM 
    ;

statement
    : 'var' ID ('=' expression)? ';'              #VariableDeclarationStatement
    ;

NUM
    : INT
    | FLOAT
    | '0'
    ;

FLOAT    : SIGN? ([1-9] NUMBER* | '0')? '.' NUMBER+ EXPONENT? ;
INT      : SIGN? [1-9] NUMBER* EXPONENT? ;
EXPONENT : ([eE] SIGN? NUMBER+) ; 
NUMBER   : [0-9] ;
SIGN     : [+-] ;
ID       : LETTER (LETTER | NUMBER)* ;
LETTER   : [a-zA-Z] ;

WS           : [ \t\n\r]+ -> skip ; // channel(HIDDEN) 
COMMENT      : '/*' .*? '*/' -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
