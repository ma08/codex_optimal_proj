#!/usr/bin/python3

import sys

N = int(sys.stdin.readline())

def solve(n):
    return n // 3 if n % 3 == 0 else n // 3 - 1

print(solve(N))
