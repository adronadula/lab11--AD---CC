# https://github.com/adronadula/lab11--AD---CC
# Partner 1: Aditya Dronadula
# Partner 2: Canran Cui

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("a cannot be 0")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Argument must be positive")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(a)
    except TypeError:
        raise ValueError("Input must be a number")


def hypotenuse(a, b):
    return math.hypot(a, b)