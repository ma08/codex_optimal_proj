
import sys, re

def solve(expr, debug=False):
    return eval(expr)

def bf_solve(expr, debug=False):
    return eval(expr)

def encode(expr, debug=False):
    result = bf_solve(expr, debug)
    if debug:
        print(result)
    return result

def main():
    expr = sys.stdin.readline().strip()
    encode(expr)

if __name__ == '__main__':
    main()
