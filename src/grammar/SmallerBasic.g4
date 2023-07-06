// SmallerBasic grammar for ANTLR4
grammar SmallerBasic;

program
    : statement+ EOF
    ;

statement
    : ID EQ expression NEWLINE? //';' 
    ;



expression
    : additiveExpression
    /* | additiveStringExpression */
    /* | multiplicativeExpression */
    /* | literal */
    /* | ID */
    ;

additiveStringExpression
    : atomString (PLUS  atomString)*
    ;

additiveExpression
    : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
    ;

multiplicativeExpression
    : atom ((MUL | DIV) atom)*
    ;

atomString
    : STRING_LITERAL
    | ID
    ;

atom
    : NUMBER_LITERAL
    | ID
    ;

literal
    : NUMBER_LITERAL 
    | STRING_LITERAL
    | BOOLEAN_LITERAL
    ;

NUMBER_LITERAL
    : INT
    | FLOAT
    | '0'
    ;

STRING_LITERAL
    : '"' ~["\u0000-\u001F\u007F]* '"' // '"' ~[\r\n"]* '"' 
    ;

BOOLEAN_LITERAL
    : 'true'
    | 'false'
    ;

// PARANTHESIS
LPAREN
    : '('
    ;

RPAREN
    : ')'
    ;

// ARITMETHIC OPERATORS
PLUS     
    : '+' 
    ;

MINUS
    : '-' 
    ;

MUL      
    : '*' 
    ;

DIV
    : '/' 
    ;

// RELATIONAL OPERATORS
GT
    : '>'
    ;
    
LT
    : '<'
    ;
    
EQ
    : '='
    ;

GTEQ
    : '>='
    ;

LTEQ
    : '<='
    ;

NEQ
    : '<>'
    ;

RELATIONAL_OPERATOR
    : GT
    | LT
    | EQ
    | GTEQ
    | LTEQ
    | NEQ
    ;

// ====================
ID       
    : CHAR (CHAR | NUM | '_')* 
    ;

INT      
    : SIGN? [1-9] NUM* EXPONENT? 
    ;

FLOAT    
    : SIGN? ([1-9] NUM* | '0')? '.' NUM+ EXPONENT? 
    ;

EXPONENT 
    : ([eE] SIGN? NUM+) 
    ; 

SIGN     
    : PLUS
    | MINUS
    ;

NUM   
    : [0-9] 
    ;

CHAR   
    : [a-zA-Z] 
    ;

WS           : [ \t\n\r]+    -> skip ; // channel(HIDDEN) 
COMMENT      : '/*' .*? '*/' -> skip ;
NEWLINE      : '\r'? '\n' ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
