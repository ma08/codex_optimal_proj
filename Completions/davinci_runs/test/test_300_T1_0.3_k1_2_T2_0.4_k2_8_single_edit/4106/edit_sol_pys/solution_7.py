import sys
sys.setrecursionlimit(10**7)

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

dp = [[-1] * (x + 1) for _ in range(n + 1)]

# dp[i][j] = i番目までの花を使って、j本の花を作る時の最大値
def solve(i, j):
    if j < 0:
        return -1
    if dp[i][j] != -1:
        return dp[i][j]
    if i == 0:
        dp[i][j] = 0
        return dp[i][j]
    if j == 0:
        dp[i][j] = 0
        return dp[i][j]
    if j < k:
        dp[i][j] = solve(i - 1, j)
        return dp[i][j]
    dp[i][j] = max(solve(i - 1, j), solve(i - k, j - k) + sum(a[i - k:i]))
    return dp[i][j]

print(solve(n, x))
