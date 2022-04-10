

# SOLUTION

import sys

input = sys.stdin.readline

n = int(input())
s = input().strip()

dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
dp[0][0] = 1

for i in range(n):
    for j in range(n + 1):
        if dp[i][j] > 0:
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j - 1] += dp[i][j]

print(dp[n][s.count('(') - s.count(')')])