import ply.lex as lex
import ply.yacc as yacc 

#reserve token dictionaries 
reserved_tk = {
    'var' : 'VAR',
    'int' : 'INT',
    'def' : 'DEF',
    'if' : 'IF',
    'else' : 'ELSE'
}
 # List of token names.   This is always required
tokens = ['PLUS', 'MINUS', 'STAR',
    'DIVIDE','LPAREN','RPAREN', 'ID',
    'NEWLINE','error','NUM','SEMI',
    'LBRACE','RBRACE','COLON',
    'EQ','NE','LT','GT',
    'BECOMES','COMMA',
    'SLASH','PCT','LE',
    'GE','ARROW','WHITESPACE',
    'COMMENT'
] + list(reserved_tk.values())
 
 # Regular expression rules for simple tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_STAR   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SLASH = r'\/'
t_PCT = r'\%'
t_COMMA = ','
t_SEMI = r'\;'
t_COLON = r'\:'
t_EQ = '=='
t_NE = '!='
t_LE = r'<='
t_GE = r'>='
t_ARROW = r'=>'
t_LT = r'\<'
t_GT = r'\>'
t_BECOMES = '\='
t_ignore  = ' \t'





def t_DEF(t):
    r'def'
    t.type = reserved_tk.get(t.value, 'DEF')    
    return t

def t_VAR(t):
    r'var'
    t.type = reserved_tk.get(t.value, 'VAR')    
    return t

def t_INT(t):
    r'int'
    t.type = reserved_tk.get(t.value, 'INT')    
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_tk.get(t.value,'ID')
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_WHITESPACES(t):
    r's'
    t.value = str(t.value)
    return t
def t_COMMENT(t):
    r'\#.*'
    pass


data = '''  def f(a:Int, b:Int):Int = { var c:Int;
                def g(a:Int, b:(Int)=>Int):Int = { b(a)}
                    def h(c:Int):Int = {
                        def g():Int = {c-b}
                        g() 
            }
            c = a+b;
            g(c,h) 
            pichula 
            INT
            adkpadas
#
            var
            #This is a comment 
            \n
            lol
            def
            >=
            <
            <=
            =>
    '''


if __name__ == '__main__':
    lexer = lex.lex()
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token: 
            break
        print(token)