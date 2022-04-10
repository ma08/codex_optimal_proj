# Solution
n = int(input())
a = list(map(int, input().split()))

a.sort()

dp = [0] * n
dp[0] = 1

for i in range(1, n):
    dp[i] = dp[i-1]
    for j in range(i-1, -1, -1):
        if abs(a[i] - a[j]) <= 5:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
