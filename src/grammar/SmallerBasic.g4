// SmallerBasic grammar for ANTLR4
grammar SmallerBasic;

program
    : statement+ EOF
    ;

expression
    : INT                                         #IntExpression 
    ;

statement
    : 'var' ID ('=' expression)? ';'              #VariableDeclarationStatement
    ;

ID: LETTER (LETTER | [0-9])* ;
INT: [0-9]+ ;
LETTER : [a-zA-Z] ;
WS: [ \t\n\r]+ -> skip ;
