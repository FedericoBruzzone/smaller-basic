// SmallerBasic grammar for ANTLR4
grammar SmallerBasic;

program
    : statement+ EOF
    ;

statement
    : declarationStatement
    | whileStatement
    | forStatement
    | ifStatement
    | labelStatement
    | gotoStatement
    ;

declarationStatement //(EQ expression)?
    : ID EQ expression
    | ID (LSQUARE arithmeticalExpression RSQUARE)+ EQ expression     
    ;

labelStatement
    : ID COLON
    ;

gotoStatement
    : GOTO ID
    ;

ifStatement
    : IF LROUND logicalExpression RROUND THEN statement+ ENDIF
    | IF LROUND logicalExpression RROUND THEN statement+ ELSE statement+ ENDIF
    ;

whileStatement
    : WHILE LROUND logicalExpression RROUND statement+ ENDWHILE
    ;

forStatement
    : FOR ID EQ arithmeticalExpression TO arithmeticalExpression statement+ ENDFOR
    | FOR ID EQ arithmeticalExpression TO arithmeticalExpression STEP arithmeticalExpression statement+ ENDFOR
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
    | LROUND logicalExpression RROUND
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
    | ('-')? LROUND arithmeticalExpression RROUND 
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

LROUND
    : '('
    ;

RROUND
    : ')'
    ;


LSQUARE
    : '['
    ;

RSQUARE
    : ']'
    ;

COLON
    : ':'
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

IF
    : 'If'
    ;

THEN
    : 'Then'
    ;

ELSE
    : 'Else'
    ;

ENDIF
    : 'EndIf'
    ;

WHILE
    : 'While'
    ;

ENDWHILE
    : 'EndWhile'
    ;

FOR
    : 'For'
    ;

TO
    : 'To'
    ;

STEP
    : 'Step'
    ;

ENDFOR
    : 'EndFor'
    ;

GOTO
    : 'Goto'
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

fragment EXPONENT 
    : ([eE] ('+' | '-')? NUM+) 
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
