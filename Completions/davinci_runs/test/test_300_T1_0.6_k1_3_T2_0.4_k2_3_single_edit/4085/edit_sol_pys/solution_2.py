#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def get_input():
    t = int(sys.stdin.readline())
    for i in range(t):
        n = int(sys.stdin.readline())
        d = list(map(int, sys.stdin.readline().split()))
        d.sort()
        yield n, d

def solve(n, d):
    if n == 1:
        return d[0] * 2
    if d[0] * d[-1] % d[-2] != 0:
        return d[0] * d[-1]
    else:
        return -1

if __name__ == '__main__':
    for n, d in get_input():
        print(solve(n, d))
