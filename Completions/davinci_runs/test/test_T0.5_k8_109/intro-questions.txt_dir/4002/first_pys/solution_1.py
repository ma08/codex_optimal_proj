

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0:
            dp[i][j] = a[i][j]
        else:
            if j == 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + 1]) + a[i][j]
            elif j == m - 1:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + a[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1]) + a[i][j]

print(dp[n - 1][m // 2])