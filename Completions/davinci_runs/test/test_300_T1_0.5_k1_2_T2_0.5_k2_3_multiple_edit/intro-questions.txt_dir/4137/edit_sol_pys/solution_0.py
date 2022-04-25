


def bfs_eval(expr):
    pass
import sys, re

def solve(expr):
    result = eval(expr)
    print(result)
    return result

def bfs_solve(expr):
    result = bfs_eval(expr)
    return result
    print(result)

def main():
    expr = sys.stdin.readline().strip()
    # print(expr)
    solve(expr)
    # bfs_solve(expr)

if __name__ == '__main__':
    main()
