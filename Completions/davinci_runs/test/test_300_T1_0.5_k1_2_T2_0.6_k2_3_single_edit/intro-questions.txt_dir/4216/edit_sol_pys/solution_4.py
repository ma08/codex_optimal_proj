#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AOJ DPL_1_B: Knapsack Problem
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B
"""

import math

def main():
    n, w = list(map(int, input().split()))
    v = []
    ws = []
    for _ in range(n):
        vi, wi = list(map(int, input().split()))
        v.append(vi)
        ws.append(wi)

    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(w+1):
            if j < ws[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-ws[i-1]] + v[i-1])

    print(dp[n][w])

if __name__ == '__main__':
    main()
