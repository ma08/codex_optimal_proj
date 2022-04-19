#!/usr/bin/env python3

import sys


def solve(n, m):
    if n == 1:
        return 0
    if n == 2:
        return m
    return (m - n + 1) * 2


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print(solve(n, m))
