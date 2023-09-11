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
    : ID EQ expression                                                                                            # VariableDeclarationStatement
    | ID (LSQUARE arithmeticalExpression RSQUARE)+ EQ expression                                                  # ArrayDeclarationStatement
    ;

labelStatement
    : ID COLON
    ;

gotoStatement
    : GOTO ID
    ;

ifStatement
    : IF LROUND logicalExpression RROUND THEN statement+ ELSE statement+ ENDIF                                    # IfStatementWithElse
    | IF LROUND logicalExpression RROUND THEN statement+ ENDIF                                                    # IfStatementWithoutElse
    ;

whileStatement
    : WHILE LROUND logicalExpression RROUND statement+ ENDWHILE                                                   # WhileStatementStandard
    ;

forStatement
    : FOR ID EQ arithmeticalExpression TO arithmeticalExpression statement+ ENDFOR                                # ForStatementStandard
    | FOR ID EQ arithmeticalExpression TO arithmeticalExpression STEP arithmeticalExpression statement+ ENDFOR    # ForStatementWithStep
    ;

subroutineStatement
    : SUB ID statement+ ENDSUB                                                                                    # SubroutineStatementStandard
    ;

callSubroutineStatement
    : ID LROUND RROUND                                                                                            # CallSubroutineStatementStandard
    ;

libraryStatement
    : ID DOT ID LROUND expression (COMMA expression)* RROUND                                                      # LibraryStatementWithParameters
    | ID DOT ID LROUND RROUND                                                                                     # LibraryStatementWithoutParameters
    ;

arrayAccess
    : ID (LSQUARE arithmeticalExpression RSQUARE)+                                                                # ArrayAccessStandard
    ;

// ======================================================
// ==================== EXPRESSIONS =====================
// ======================================================
expression
    : logicalExpression
    | arithmeticalExpression
    | stringExpression
    ;

//  ==================== LOGICAL AND BOOLEAN EXPRESSIONS ====================

logicalExpression
    : booleanExpression ((AND | OR) booleanExpression)*
    ;

booleanExpression
    : arithmeticalExpression (GT | LT | EQ | GTEQ | LTEQ | NEQ) arithmeticalExpression                            # BooleanArithmeticalExpression
    | stringExpression (GT | LT | EQ | GTEQ | LTEQ | NEQ) stringExpression                                        # BooleanStringExpression
    | atomBoolean                                                                                                 # BooleanAtomExpression
    ;

atomBoolean
    : BOOLEAN                                                                                                     # AtomBooleanBoolean
    | ID                                                                                                          # AtomBooleanId
    | LROUND logicalExpression RROUND                                                                             # AtomBooleanParenthesis
    | libraryStatement                                                                                            # AtomBooleanLibraryStatement
    | arrayAccess                                                                                                 # AtomBooleanArrayAccess
    ;

//  ==================== ARITHMETICAL EXPRESSIONS ====================
arithmeticalExpression
    : additiveExpression
    ;

additiveExpression
    : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
    ;

multiplicativeExpression
    : unaryAtomNumber ((MUL | DIV) multiplicativeExpression)*
    ;

unaryAtomNumber
    : (PLUS | MINUS)? atomNumber
    ;

atomNumber
    : INT                                                                                                         # AtomNumberInt
    | FLOAT                                                                                                       # AtomNumberFloat
    | ID                                                                                                          # AtomNumberId
    | LROUND additiveExpression RROUND                                                                            # AtomNumberParenthesis
    | libraryStatement                                                                                            # AtomNumberLibraryStatement
    | arrayAccess                                                                                                 # AtomNumberArrayAccess
    ;

//  ==================== STRING EXPRESSIONS ====================
stringExpression
    : additiveStringExpression
    ;

additiveStringExpression
    : atomString (PLUS  additiveStringExpression)*
    ;

atomString
    : STRING                                                                                                      # AtomStringLiteral
    | ID                                                                                                          # AtomStringId
    | LROUND stringExpression RROUND                                                                              # AtomStringParenthesis
    | libraryStatement                                                                                            # AtomStringLibraryStatement
    | arrayAccess                                                                                                 # AtomStringArrayAccess
    ;

// ================================================
//  ==================== LEXER ====================
// ================================================
STRING
    : '"' ~["\u0000-\u001F\u007F]* '"' // '"' ~[\r\n"]* '"'
    ;

BOOLEAN
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

COMMA
    : ','
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
NEWLINE      : '\r'? '\n' ;
LINE_COMMENT : '\'' ~[\r\n]* -> skip ;
COMMENT      : '\'*' .*? '*\'' -> skip ;
// COMMENT      : '/*' .*? '*/' -> skip ;
// LINE_COMMENT : '//' ~[\r\n]* -> skip ;
