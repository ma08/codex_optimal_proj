
n, m = map(int, input().split())
a = [0] * m
for i in range(m):
    a[i] = int(input())

dp = [0] * (n + 2)
dp[1] = 1 # n = 1 の時の解
dp[2] = 1 # n = 2 の時の解

for i in range(3, n + 2):
    if i not in a:
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

print(dp[n + 1])
