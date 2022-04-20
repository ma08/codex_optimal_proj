
n = int(input())
a = list(map(int, input().split())) + [0]
dp = [0] * n
for i in range(n - 1, -1, -1):
    dp[i] = max(dp[i + 1], a[i] - a[i + 1] + dp[i + 2])
print(dp[0])
