
import sys

n, h, l, r = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

dp = [[0] * h for _ in range(n)]

for i in range(1, n):
    for j in range(h):  # 前日の睡眠時間
        dp[i][j] = max(dp[i-1][j],dp[i-1][(j+a[i-1])%h])

        if l <= (j+a[i-1]) % h <= r:
            dp[i][j] = max(dp[i][j],dp[i-1][j]+1)

print(max(dp[n-1]))
