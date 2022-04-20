

import sys

def solve(expr):
    return eval(expr)

def bf_solve(expr):
    return eval(expr)

def encode(expr):
    return bf_solve(expr)

def main():
    expr = sys.stdin.readline().strip()
    print(solve(expr))

if __name__ == '__main__':
    main()
