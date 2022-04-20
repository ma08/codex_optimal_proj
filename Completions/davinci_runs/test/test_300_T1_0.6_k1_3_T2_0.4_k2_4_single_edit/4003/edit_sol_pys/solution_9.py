#!/usr/bin/python3


import sys

def solve(a, n):
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        dp[i] = 1
        for j in range(i):
            if a[i] > a[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)

n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().split()]
print(solve(a, n))
