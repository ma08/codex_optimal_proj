
def solve(n, m, a, b):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

n = int(input())
m = int(input())
a = [int(input()) for _ in range(n)]
b = [int(input()) for _ in range(m)]
print(solve(n, m, a, b))
