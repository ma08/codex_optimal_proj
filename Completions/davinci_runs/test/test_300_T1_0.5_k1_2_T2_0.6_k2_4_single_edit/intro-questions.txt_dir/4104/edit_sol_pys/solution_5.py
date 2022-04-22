
from math import *
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

def main():
    expression = input()
    result = parse_expr(expression)
    print(result)

if __name__ == "__main__":
    main()
