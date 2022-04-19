# -*- coding: utf-8 -*-

import math
import sys

def main():
    N, A, B, C = map(int, sys.stdin.readline().split())
    l = [int(sys.stdin.readline()) for _ in range(N)]
    l.sort()
    print(solve(l, A, B, C))

def solve(l, A, B, C):
    if len(l) == 0:
        return math.inf
    if len(l) == 1:
        return 10 if l[0] < A else 0
    else:
        return 10 + solve(l[1:], A - l[0], B - l[0], C - l[0])

if __name__ == '__main__':
    main()
