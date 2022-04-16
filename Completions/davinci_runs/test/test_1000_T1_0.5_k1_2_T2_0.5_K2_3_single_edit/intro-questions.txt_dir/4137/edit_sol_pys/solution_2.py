

import sys, re

def solve(expr):
    try:
        result = eval(expr)
    except:
        result = None
    print(result)
    return result

def bf_solve(expr):
    try:
        result = eval(expr)
    except:
        result = None
    #print(result)
    return result

def encode(expr):
    result = bf_solve(expr)
    print(result)

def main():
    expr = sys.stdin.readline().strip()
    # print(expr)
    solve(expr)
    # encode(expr)

if __name__ == '__main__':
    main()
