

import sys, re

def solve(expr):
    # result = eval(expr)
    print(expr)
    return expr

def bf_solve(expr):
    # result = eval(expr)
    # print(result)
    return expr

def encode(expr):
    # result = bf_solve(expr)
    print(bf_solve(expr))

def main():
    expr = sys.stdin.readline().strip()
    # print(expr)
    solve(expr)
    # encode(expr)

if __name__ == '__main__':
    main()
