from math import factorial
from math import sqrt
from math import pi
from math import e
from math import sin
from math import cos
from math import tan
from math import asin
from math import acos
from math import atan
from math import sinh
from math import cosh
from math import tanh
from math import asinh
from math import acosh
from math import atanh
from math import log
from math import log2
from math import log10
from math import exp
from math import floor
from math import ceil


def get_input():
    return input("Enter a function: ")

def get_variables(input):
    variables = []
    for i in range(len(input)):
        if input[i] == "x":
            variables.append(i)
    return variables

def get_operators(input):
    operators = []
    for i in range(len(input)):
        if input[i] == "^":
            operators.append(i)
    return operators

def get_numbers(input):
    numbers = []
    for i in range(len(input)):
        if input[i] == "x":
            numbers.append(i)
    return numbers

def get_sides(input, variables):
    sides = []
    for i in range(len(variables)):
        sides.append(input[:variables[i]])
        sides.append(input[variables[i]+1:])
    return sides

def get_numbers(input, variables):
    numbers = []
    for i in range(len(variables)):
        numbers.append(input[:variables[i]])
        numbers.append(input[variables[i]+1:])
    return numbers

def get_operators(input, variables):
    operators = []
    for i in range(len(variables)):
        operators.append(input[:variables[i]])
        operators.append(input[variables[i]+1:])
    return operators





























































































































































































































































































































































































































































































































































































































































































































