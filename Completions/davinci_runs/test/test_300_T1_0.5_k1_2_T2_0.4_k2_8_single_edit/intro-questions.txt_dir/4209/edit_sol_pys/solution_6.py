#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def solve(n, a):
    dp = [1] * n  # dp[i] = LIS of a[0:i+1]
    for i in range(1, n):  # dp[i] = max(dp[i], dp[j] + 1) for j in [0:i)
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    print(solve(n, a))

if __name__ == '__main__':
    main()
