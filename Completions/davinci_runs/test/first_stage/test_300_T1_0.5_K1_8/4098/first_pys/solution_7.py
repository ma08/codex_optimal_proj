

n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

for i in range(1, k + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i][j - 1]
        for l in range(j - 1, 0, -1):
            if a[j - 1] - a[l - 1] <= 5:
                dp[i][j] = max(dp[i][j], dp[i - 1][l - 1] + j - l)

print(dp[-1][-1])