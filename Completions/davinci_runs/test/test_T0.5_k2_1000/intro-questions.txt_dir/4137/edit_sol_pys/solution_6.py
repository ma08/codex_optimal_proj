

import sys

def solve(expr):
    result = eval(expr)
    return result

def bf_solve(expr):
    result = eval(expr)
    return result

def encode(expr):
    result = bf_solve(expr)

def main():
    expr = sys.stdin.readline().strip()
    solve(expr)

if __name__ == '__main__':
    main()
