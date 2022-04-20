
n, k, x = map(int, input().split())
a = list(map(int, input().split()))

# if x < k:
#     print(-1)
#     exit()

dp = [[0] * (x + 1) for _ in range(n + 2)]

for i in range(1, n + 2):
    for j in range(1, x + 1):
        if j < k:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - k][j - k] + sum(a[i - k - 1:i - 1]))

print(dp[n][x])
