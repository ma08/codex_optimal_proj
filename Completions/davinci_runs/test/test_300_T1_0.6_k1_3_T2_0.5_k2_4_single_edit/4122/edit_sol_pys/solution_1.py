

import sys

def solve():
    h, n = map(int, sys.stdin.readline().split())
    d = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        h += d[i]
        if h <= 0:
            return i + 1
    return -1

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    print(solve())
