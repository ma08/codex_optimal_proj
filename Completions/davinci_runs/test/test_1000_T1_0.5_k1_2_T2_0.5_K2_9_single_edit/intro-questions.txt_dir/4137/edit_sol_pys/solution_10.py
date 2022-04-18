

import sys, re

def solve(expr):
    # result = eval(expr)
    # print(result)
    # return result
    return expr

def bf_solve(expr):
    result = eval(expr)
    # print(result)
    return result
def encode_char(c):
    return c.encode("utf-8")


def encode(expr):
    result = ''.join(map(encode_char, bf_solve(expr)))
    print(result)

def main():
    expr = sys.stdin.readline().strip()
    # print(solve(expr))
    encode(expr)

if __name__ == '__main__':
    main()
