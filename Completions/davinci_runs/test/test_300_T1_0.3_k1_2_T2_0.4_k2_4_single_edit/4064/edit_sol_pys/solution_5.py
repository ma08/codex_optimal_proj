#!/usr/bin/env python3

n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * h
dp[0] = 1

for i in range(n):
    dp2 = dp[:]
    for j in range(h):
        if dp[j]:
            dp2[(j + a[i]) % h] = 1
            dp2[(j + a[i] - 1) % h] = 1
    dp = dp2

print(sum(dp[l:r + 1]))
