// SmallerBasic grammar for ANTLR4
grammar SmallerBasic;

program
    : statement+ EOF
    ;

// ======================================================
//  ==================== STATEMENTS =====================
// ======================================================
statement
    : declarationStatement
    | whileStatement
    | forStatement
    | ifStatement
    | labelStatement
    | gotoStatement
    | subroutineStatement
    | callSubroutineStatement
    | libraryStatement
    ;

declarationStatement //(EQ expression)?
    : ID EQ expression                                            # VariableDeclarationStatement
    | ID (LSQUARE arithmeticalExpression RSQUARE)+ EQ expression  # ArrayDeclarationStatement
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

subroutineStatement
    : SUB ID statement+ ENDSUB
    ;

callSubroutineStatement
    : ID LROUND RROUND
    ;

libraryStatement
    : ID (DOT ID)+ LROUND expression? RROUND
    ;

// ======================================================
// ==================== EXPRESSIONS ====================
// ======================================================
expression
    : literal
    | logicalExpression
    | arithmeticalExpression 
    | stringExpression 
    ;

//  ==================== LOGICAL AND BOOLEAN EXPRESSIONS ====================
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
    | LROUND logicalExpression RROUND
    | libraryStatement
    | ID 
    ;

//  ==================== ARITHMETICAL EXPRESSIONS ====================
arithmeticalExpression
    : additiveExpression
    ;

additiveExpression
    : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
    ;

multiplicativeExpression
    : atomNumber ((MUL | DIV) multiplicativeExpression)*
    ;

atomNumber
    : signedInt                                     # AtomIntLiteral 
    | signedFloat                                   # AtomFloatLiteral
    | signedId                                      # AtomNumberId
    | ('-')? LROUND arithmeticalExpression RROUND   # AtomNumberArithmeticalExpression 
    | ('-')? libraryStatement                       # AtomNumberLibraryStatement
    ;

//  ==================== STRING EXPRESSIONS ====================
stringExpression
    : additiveStringExpression
    ;

additiveStringExpression
    : atomString (PLUS  additiveStringExpression)* 
    ;

atomString
    : string                                        # AtomStringLiteral
    | ID                                            # AtomStringId  
    | libraryStatement                              # AtomStringLibraryStatement
    ;

//  ==================== LITERALS ====================
literal
    : signedInt
    | signedFloat
    | string 
    | boolean
    | signedId
    ;

signedInt
    : ('-' | '+')? INT            
    ;

signedFloat
    : ('-' | '+')? FLOAT          
    ;


string
    : STRING_LITERAL              
    ;

boolean
    : BOOLEAN_LITERAL             
    ;

signedId
    : ('-' | '+')? ID             
    ;

// ================================================
//  ==================== LEXER ====================
// ================================================
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

DOT
    : '.'
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

SUB
    : 'Sub'
    ;

ENDSUB
    : 'EndSub'
    ;

ID       
    : CHAR (CHAR | NUM | '_')* 
    ;

INT      
    : '0' 
    | [1-9] NUM* // EXPONENT? 
    ;

FLOAT    
    : ([1-9] NUM* | '0')? ('.')? NUM+ EXPONENT? 
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
