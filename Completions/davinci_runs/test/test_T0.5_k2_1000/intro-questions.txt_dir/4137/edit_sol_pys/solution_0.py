

import sys, re

def solve(expr):
    result = eval(expr)
    print(result)
    return result

def encode(expr):
    result = solve(expr)
    print(result) 


def main():
    expr = sys.stdin.readline().strip()
    encode(expr)

if __name__ == '__main__':
    main()
