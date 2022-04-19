

import sys, re

def solve(expr):
    try:
        result = eval(expr)
        print(result)
    except:
        print("Error")
    return result

def bf_solve(expr):
    result = ""
    try:
        result = eval(expr)
        # print(result)
    except:
        print("Error")
    return result

def encode(expr):
    try:
        result = bf_solve(expr)
        print(result)
    except:
        print("Error")

def main():
    expr = sys.stdin.readline().strip()
    # print(expr)
    solve(expr)
    # encode(expr)

if __name__ == '__main__':
    main()
