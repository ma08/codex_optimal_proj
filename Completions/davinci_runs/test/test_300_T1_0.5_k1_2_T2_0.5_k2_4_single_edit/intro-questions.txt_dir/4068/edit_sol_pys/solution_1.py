
n, k = map(int, input().split())
dp = [0] * (k + 1)
dp[0] = 1
for i in range(1, k + 1):
    for j in range(1, n + 1):
        if i - j >= 0:
            dp[i] += dp[i - j]
print(dp[k])
