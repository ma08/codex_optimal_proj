

#Solution

import sys

def readline(): return sys.stdin.readline().strip()

n, m, k = map(int, readline().split())
a = [list(map(int, readline().split())) for _ in range(n)]

dp = [[0] * (m // 2 + 1) for _ in range(n)]

for i in range(n):
    for j in range(m // 2 + 1):
        if j == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = max([dp[i - 1][j], dp[i - 1][j - 1] + a[i][j * 2 - 2], dp[i - 1][j - 1] + a[i][j * 2 - 1]])

print(dp[n - 1][m // 2])