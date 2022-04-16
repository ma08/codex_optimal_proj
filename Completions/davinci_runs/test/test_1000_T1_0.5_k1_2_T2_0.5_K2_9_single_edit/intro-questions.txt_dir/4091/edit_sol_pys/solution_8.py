#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-03 22:53:58
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-03 23:17:55

import sys

n, k = map(int, input().split())
a = list(map(int, input().split()))

# dp[i][j] = max profit for i problems in j days (1-based)
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if i < j:
            continue
        dp[i][j] = max(dp[i - l][j - 1] + max(a[i - l:i]) for l in range(1, min(k, i) + 1))

print(dp[n][k])

i, j = n, k
ans = []
while j > 0:
    for l in range(1, min(k, i) + 1):
        if dp[i][j] == dp[i - l][j - 1] + max(a[i - l:i]):
            ans.append(l)
            i -= l
            j -= 1
            break

print(*ans[::-1])
