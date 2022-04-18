
# coding=utf-8

import sys


def solve(n, k):
    return n * (n - 1) // 2 - k


if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for i in range(t):
        n, k = map(int, sys.stdin.readline().split())
        print(solve(n, k))
