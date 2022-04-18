# -*- coding: utf-8 -*-

import sys

N = int(sys.stdin.readline())
h = list(map(int,sys.stdin.readline().split()))
h.append(0)

dp = [0]

for i in range(1,N+1):
    dp.append(min(dp[i-1]+abs(h[i]-h[i-1]), dp[i-2]+abs(h[i]-h[i-2])))

print(dp[N])
