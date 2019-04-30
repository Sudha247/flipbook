import ply.lex as lex
import ply.yacc as yacc
from fpdf import FPDF
from pathlib import Path
import sys
from PIL import Image
import os

#Initializing the PDF
pdf = FPDF()

# Tokens

tokens = ('NUMBER', 'IMAGE', 'COMMENT', 'SCALE', 'MOVE', 'ROTATE')

t_ignore = ' \t\n'
t_IMAGE = r'[a-zA-Z0-9]+.jpg'
t_COMMENT = r'//[\w\d\'*=!@#$%^&*() \t]*'
t_SCALE = 'scale'
t_MOVE = 'move'
t_ROTATE = 'rotate'

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

def p_show_scale(p):
    '''statement : NUMBER NUMBER IMAGE SCALE NUMBER
                | NUMBER NUMBER IMAGE SCALE NUMBER COMMENT'''
    #debug
    print(p[1], p[2], p[3], p[4], p[5])
    diff = p[2] - p[1]
    width = 100
    height = 100 # Static Initial values
    wdiff = (width * p[5])/diff
    hdiff = (height * p[5])/diff

    for i in range(p[1], p[2]+1):
        pdf.add_page()
        pdf.image(p[3], w = width, h = height)
        width = width + wdiff
        height = height + hdiff

def p_show_move(p):
    '''statement : NUMBER NUMBER IMAGE MOVE NUMBER NUMBER
                | NUMBER NUMBER IMAGE MOVE NUMBER NUMBER COMMENT
    '''
    print(p[1], p[2], p[3], p[4], p[5], p[6])
    x = 0
    y = 0
    diff = p[2] - p[1]
    xdiff = p[5]/diff
    ydiff = p[6]/diff

    for i in range(p[1], p[2]+1):
        pdf.add_page()
        pdf.image(p[3],x,y)
        x = x + xdiff
        y = y + ydiff

def p_show_rotate(p):
    '''statement : NUMBER NUMBER IMAGE ROTATE NUMBER
    '''
    print(p[1], p[2], p[3], p[4], p[5])
    diff = p[2] - p[1]
    rot = p[5]/diff
    r = 0
    for i in range(p[1], p[2]+1):
        im = Image.open(p[3])
        temp = im.rotate(r)
        #temp.show()
        r = r + rot
        print(r)
        temp.save("test"+str(i)+".jpg", "JPEG")
        pdf.add_page()
        pdf.image("test"+str(i)+".jpg")
        os.remove("test"+str(i)+".jpg")


def p_error(p):
    print("Syntax error")

yacc.yacc()

#print("CL Arguments = ", len(sys.argv))
#print(sys.argv[1], sys.argv[3])

# Command line arguments :-
# 1 -> input program
# 3 -> output pdf

cf = Path(sys.argv[1])
if cf.is_file():
    ipfile = open(sys.argv[1], "r")
    for line in ipfile:
        yacc.parse(line)
else:
    print(sys.argv[1], "file not found!")

pdf.output(sys.argv[3], "F")
