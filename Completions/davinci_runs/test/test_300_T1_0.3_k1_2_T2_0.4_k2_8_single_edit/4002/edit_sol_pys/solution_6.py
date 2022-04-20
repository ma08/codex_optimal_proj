#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 14:27:43 2019

@author: y56
"""

n, m, k = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

dp = [[0] * (m + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j <= m // 2:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1] + a[i - 1][j - 1])
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[n][m - m // 2])
