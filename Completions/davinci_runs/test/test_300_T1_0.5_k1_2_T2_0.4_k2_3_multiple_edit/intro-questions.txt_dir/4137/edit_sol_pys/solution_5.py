

import sys, re

def solve(expr):
    result = eval(expr)
    print(result)
    return result

def encode(expr):
    result = eval(expr)
    print(str(result))

def main():
    expr = sys.stdin.readline().strip()
    # solve(expr)
    encode(expr)

if __name__ == '__main__':
    main()
