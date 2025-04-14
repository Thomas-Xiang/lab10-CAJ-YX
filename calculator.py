# github link: https://github.com/Thomas-Xiang/lab10-CAJ-YX.git
# https://github.com/CelineJaime/lab10-CAJ-YX.git
# Partner 1: Celine Jaime
# Partner 2: Thomas Xiang

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(a)
    except TypeError:
        raise ValueError("Input must be a number.")

def hypotenuse(a, b):
    try:
        return math.hypot(a,b)
    except TypeError:
        raise ValueError("Inputs must be numbers.")

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
    
def logarithm(a, b):
    if a <= 0 or a==1 or b <=0:
        raise ValueError("Invalid input for logarithm.")
    return math.log(b, a)

def exp(a, b):
    return a ** b





