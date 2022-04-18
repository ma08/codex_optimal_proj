
n = int(input())
a = list(map(int, input().split()))

dp = [[0]*n for i in range(n)]

for i in range(n):
    dp[i][i] = a[i]

for i in range(n):
    for j in range(i+1, n):
        dp[i][j] = dp[i][j-1] + a[j]

print(dp)
