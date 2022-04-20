

# n, h, l, r = map(int, input().split())
# a = list(map(int, input().split()))

n, h, l, r = 7, 24, 21, 23
a = [16, 17, 14, 20, 20, 11, 22]

dp = [[0] * (h + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(h):
        dp[i][j] = dp[i - 1][j]
        if l <= j <= r:
            dp[i][j] += 1
        if l <= j + a[i - 1] <= r:
            dp[i][j] = max(dp[i][j], 1 + dp[i - 1][j + a[i - 1] - 1])

print(max(dp[-1]))