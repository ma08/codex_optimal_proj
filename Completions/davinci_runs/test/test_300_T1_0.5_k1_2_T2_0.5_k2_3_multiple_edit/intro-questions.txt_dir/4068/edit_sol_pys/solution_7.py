#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import numpy as np
sys.setrecursionlimit(10**7)


def main():
    N, M = map(int, input().split())
    broken_stairs = [int(input()) - 1 for _ in range(M)]
    broken_stairs.sort()
    dp[1] = 2
    dp[2] = 4
    for i in range(3, N+1):
        if i in broken_stairs: continue
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[N] % 1000000007)

if __name__ == "__main__":
    main()
