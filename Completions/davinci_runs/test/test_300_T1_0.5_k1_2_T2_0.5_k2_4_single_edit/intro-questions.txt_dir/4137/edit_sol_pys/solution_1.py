
import sys

def solve(expr):
    result = eval(expr)
    print(result, end="")
    return result

def bf_solve(expr):
    result = eval(expr)
    # print(result)
    return result

def encode(expr):
    result = bf_solve(expr)
    print(result, end="")

def main():
    expr = sys.stdin.readline().strip()
    # print(expr)
    solve(expr)
    # encode(expr)

if __name__ == '__main__':
    main()
