import sys
sys.setrecursionlimit(10 ** 7)

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0] * (x + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, x + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - k][j - 1] + sum(a[i - k:i]))
print(dp[n][x])
