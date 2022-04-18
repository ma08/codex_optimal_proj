

n, m = map(int, input().split())
a = [0] * m
for i in range(m):
    a[i] = int(input())

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    if i in a:
        dp[i] = 0
    else:
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
print(dp[n])