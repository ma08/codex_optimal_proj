#!/usr/bin/python3

import sys

def solve(n, a):
    a.sort()
    if n == 1:
        return a[0]
    elif n == 2:
        return a[1]
    else:
        return max(a[0] * a[1] * a[2], a[0] * a[1] * a[n-1])

q = int(sys.stdin.readline())
for query_number in range(q):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    print(solve(n, a))
