# https://github.com/elizapikulinski/lab11-ep-bd.git
# Partner 1: Eliza Pikulinski
# Partner 2: Briana DeStoppelaire
import math

def spare_root(a):
    if a < 0:
        raise ValueError
    return math.squrt(a)

def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return b/a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b,a)

def exp(a, b):
    a**b

