

n, h, l, r = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

dp = [[0 for i in range(h)] for j in range(n)]

dp[0][a[0] - 1] = 1
dp[0][a[0] % h] = 1

for i in range(1, n):
    for j in range(h):
        dp[i][j] = max(dp[i - 1][(j + a[i]) % h], dp[i - 1][(j + a[i] - 1) % h])

print(dp[-1][l] + dp[-1][r])