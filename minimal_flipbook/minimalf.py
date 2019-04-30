import os
import ply.lex as lex
import ply.yacc as yacc
from fpdf import FPDF
from pathlib import Path
import sys

#Initializing the PDF
pdf = FPDF()

# Tokens

tokens = ('NUMBER', 'IMAGE', 'COMMENT')

t_ignore = ' \t\n'
t_IMAGE = r'[a-zA-Z0-9]+.jpg'
t_COMMENT = r'//[\w\d\'*=!@#$%^&*() \t]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()

# Production rules

def p_comment(p):
    'statement : COMMENT'
    pass

def p_show(p):
    '''statement : NUMBER NUMBER IMAGE
                 | NUMBER NUMBER IMAGE COMMENT'''
    #debug
    print(p[1], p[2], p[3])
    config = Path(p[3])
    if config.is_file():
        for i in range(p[1], p[2]+1):
            pdf.add_page()
            pdf.image(p[3])
    else:
        print(p[3], " -> Image does not exist in the directory. Is your file name right?")

def p_error(p):
    print("Syntax error")

yacc.yacc()

#print("CL Arguments = ", len(sys.argv))
#print(sys.argv[1], sys.argv[3])

# 1 -> input program
# 3 -> output pdf

cf = Path(sys.argv[1])
if cf.is_file():
    ipfile = open(sys.argv[1], "r")
    for line in ipfile:
        yacc.parse(line)
else:
    print(sys.argv[1], "file not found!")

'''while True:
    try:
        s = input('> ')
    except EOFError:
        break
    yacc.parse(s)'''

pdf.output(sys.argv[3], "F")
