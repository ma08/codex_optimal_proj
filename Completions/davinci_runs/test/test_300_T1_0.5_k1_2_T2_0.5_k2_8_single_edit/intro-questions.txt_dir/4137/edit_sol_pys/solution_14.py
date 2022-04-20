

import sys

def solve(expr):
    result = eval(expr)
    print(result)
    return result

def bf_solve(expr):
    result = eval(expr)
    # print(result)
    return result

def encode(expr):
    result = bf_solve(expr.replace(' ', ''))
    print(result)

def main():
    expr = sys.stdin.readline().strip()
    encode(expr)

if __name__ == '__main__':
    main()
