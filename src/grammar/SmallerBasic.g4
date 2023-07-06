// SmallerBasic grammar for ANTLR4
grammar SmallerBasic;

program
    : statement+ EOF
    ;

statement
    : declarationStatement
    ;

declarationStatement
    : ID (EQ expression)? NEWLINE? //';' 
    ;

expression
    : arithmeticalExpression 
    | logicalExpression
    | stringExpression 
    | literal
    ;

logicalExpression
    : booleanExpression ((AND | OR) booleanExpression)+
    | booleanExpression
    ;

booleanExpression
    : arithmeticalExpression (GT | LT | EQ | GTEQ | LTEQ | NEQ) arithmeticalExpression
    | atomBoolean 
    ;

atomBoolean
    : boolean
    | id
    | LPAREN logicalExpression RPAREN
    ;

arithmeticalExpression
    : additiveExpression
    ;

additiveExpression
    : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)+ // #WithAdd
    | multiplicativeExpression // #NoAdd
    ;

multiplicativeExpression
    : atomNumber ((MUL | DIV) atomNumber)+
    | atomNumber
    ;

atomNumber
    : signedNumber
    | id 
    | LPAREN arithmeticalExpression RPAREN
    ;

stringExpression
    : additiveStringExpression
    ;

additiveStringExpression
    : atomString (PLUS  atomString)*
    ;

atomString
    : string
    | id
    ;

literal
    : signedNumber 
    | string 
    | boolean
    | id
    ;

signedNumber
    : ('-' | '+')? NUMBER_LITERAL
    ;

string
    : STRING_LITERAL
    ;

boolean
    : BOOLEAN_LITERAL
    ;

id
    : ('-' | '+')? ID
    ;
////////////////////////////

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

LPAREN
    : '('
    ;

RPAREN
    : ')'
    ;

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

AND
    : 'And'
    ;

OR
    : 'Or'
    ;

// ====================
ID       
    : CHAR (CHAR | NUM | '_')* 
    ;

fragment INT      
    : [1-9] NUM* EXPONENT? 
    ;

fragment FLOAT    
    : ([1-9] NUM* | '0')? '.' NUM+ EXPONENT? 
    ;

fragment SIGN
    : ('+' | '-')    
    ;

fragment EXPONENT 
    : ([eE] SIGN? NUM+) 
    ; 

fragment NUM   
    : [0-9] 
    ;

fragment CHAR   
    : [a-zA-Z] 
    ;

WS           : [ \t\n\r]+    -> skip ; // channel(HIDDEN) 
COMMENT      : '/*' .*? '*/' -> skip ;
NEWLINE      : '\r'? '\n' ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
