#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import numpy as np



def main():
    N, M = map(int, input().split())
    broken_stairs = [int(i) for i in input().split()]
    broken_stairs.sort()
    dp = np.zeros(N+1, dtype=np.int)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N+1):  # i is the current stair
        if i in broken_stairs:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % (10**9+7)  # mod
    print(dp[N])

if __name__ == "__main__":
    main()
