

import sys, re

def solve(expr):
    try:
        result = eval(expr)
    except Exception:
        result = 'ERROR'
    print(result)
    return result

def encode(expr):
    # result = solve(expr)
    # print(result)
    pass

def main():
    expr = sys.stdin.readline().strip()
    # print(expr)
    solve(expr)
    # encode(expr)

if __name__ == '__main__':
    main()
