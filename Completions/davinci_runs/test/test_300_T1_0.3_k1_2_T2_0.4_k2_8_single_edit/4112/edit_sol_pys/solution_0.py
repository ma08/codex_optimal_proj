#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 26/05/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

if x < k:
    print(-1)
else:
    dp = [[0] * (x + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, x + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - k][j - 1] + sum(a[i - k:i]))
    print(dp[n][x])
