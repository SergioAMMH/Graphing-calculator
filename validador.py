#importamos liberia

import numpy as np
from sympy import *

def validador(num):
    try:
        neval = eval(num)
        tiponum = type(neval)
        if tiponum == int or tiponum == float:
            return True
        else:
            return False
    except:
        return False
def validadorint(num):
    try:
        neval = eval(num)
        tiponum = type(neval)
        if tiponum == int:
            return True
        else:
            return False
    except:
        return False

def exprvalidador(expr):
    loc = {'sqrt': sqrt, 'sin': sin, 'cos': cos, 'tan': tan,'cot':cot, 'x':1,'sec':sec,'csc':csc ,'pi':np.pi, 'exp':np.exp}
    try: 
        expr1 = expr
        expr1 = eval(expr, loc)
        return True

    except:
        return False

def valexpr(expr):
    error = 'error'
    return error