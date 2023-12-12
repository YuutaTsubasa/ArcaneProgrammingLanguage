grammar Arcane;

prog:   stat* EOF;
stat:   expr ';';

expr:   expr ('*' | '/' | '%') expr
      | expr ('+' | '-') expr
      | varDeclaration
      | assignment
      | 'return' expr
      | atom;

varDeclaration: VAR ID ':' TYPE '=' expr;
assignment:       ID '=' expr
                | varDeclaration '=' expr;

atom:   INT
      | FLOAT
      | BOOL
      | ID
      | '(' expr ')';

TYPE: 'Int8' | 'Int16' | 'Int32' | 'Int64'
    | 'Float32' | 'Float64'
    | 'Char' | 'Bool';

VAR:    'val' | 'var';
BOOL:   'true' | 'false';
ID:     [a-zA-Z_][a-zA-Z_0-9]*;
INT:    [0-9]+;
FLOAT:  [0-9]+ '.' [0-9]* | '.' [0-9]+;
WS:     [ \t\r\n]+ -> skip;