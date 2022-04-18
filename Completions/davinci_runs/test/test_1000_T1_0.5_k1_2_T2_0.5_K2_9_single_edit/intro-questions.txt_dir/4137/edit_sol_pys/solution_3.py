
import sys, re

def solve(expr):
    return eval(expr)

def bf_solve(expr):
    result = eval(expr)
    # print(result)
    return result

def encode(expr):
    return bf_solve(expr)

def main():
    expr = sys.stdin.readline().strip()
    print(solve(expr))
    print(encode(expr))

if __name__ == '__main__':
    main()
