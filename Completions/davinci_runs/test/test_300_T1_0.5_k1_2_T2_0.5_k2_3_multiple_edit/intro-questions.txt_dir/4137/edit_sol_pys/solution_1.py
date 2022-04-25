
import math
import sys, re

def solve(expr):
    result = eval(expr)
    # print(result)
    return result

def bf_solve(expr):
    result = bf_eval(expr)
    # print(result)
    return result
def bf_eval(expr):
    expr = re.sub("\d+", "", expr)
    # print("expr",expr)
    if len(expr) == 0:
        return 0
    if len(expr) == 1:
        return 1
    if len(expr) == 2:
        return 2
    if expr[0] == '+' and expr[1] == '+':
        return bf_eval(expr[2:]) + 2
    if expr[0] == '-' and expr[1] == '-':
        return bf_eval(expr[2:]) + 2
    if expr[0] == '*' and expr[1] == '*':
        return bf_eval(expr[2:]) + 2
    if expr[0] == '/' and expr[1] == '/':
        return bf_eval(expr[2:]) + 2
    if expr[0] == '+' and expr[1] == '-':
        return bf_eval(expr[2:]) + 2
    if expr[0] == '-' and expr[1] == '+':
        return bf_eval(expr[2:]) + 2
    if expr[0] == '*' and expr[1] == '/':
        return bf_eval(expr[2:]) + 2
    if expr[0] == '/' and expr[1] == '*':
        return bf_eval(expr[2:]) + 2
    if expr[0] == '+':
        return bf_eval(expr[1:]) + 1
    if expr[0] == '-':
        return bf_eval(expr[1:]) + 1
    if expr[0] == '*':
        return bf_eval(expr[1:]) + 1
    if expr[0] == '/':
        return bf_eval(expr[1:]) + 1
    if expr[0] == '(':
        return bf_eval(expr[1:]) + 1
    if expr[0] == ')':
        return bf_eval(expr[1:]) + 1


def encode(expr):
    # print(result)
    # print(bf_solve(expr))
    print(bf_solve(expr) - result)

def main():
    expr = sys.stdin.readline().strip()
    # print(expr)
    # solve(expr)
    encode(expr)

if __name__ == '__main__':
    main()
