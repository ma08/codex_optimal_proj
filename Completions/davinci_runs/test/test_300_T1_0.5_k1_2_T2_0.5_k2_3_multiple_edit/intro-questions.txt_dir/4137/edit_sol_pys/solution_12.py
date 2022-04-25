

from collections import deque

def bfs_eval(expr):
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }

    q = deque()
    q.append(expr)

    while len(q) > 0:
        expr = q.popleft()
        print(expr)
        if re.search(r'^[0-9]+$', expr):
            return int(expr)
        for i in range(len(expr)):
            if expr[i] in ops.keys():
                expr_left = expr[:i]
                expr_right = expr[i+1:]
                q.append(str(ops[expr[i]](bfs_eval(expr_left), bfs_eval(expr_right))))
                break
    return None
import sys, re

def solve(expr):
    result = eval(expr)
    print(result)
    return result

def bfs_solve(expr):
    result = bfs_eval(expr)
    print(result)

def main():
    expr = sys.stdin.readline().strip()
    # print(expr)
    # solve(expr)
    bfs_solve(expr)

if __name__ == '__main__':
    main()
