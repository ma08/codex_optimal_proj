

n = int(input())
a = [int(x) for x in input().split()] + [0]

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][i] = a[i]
for i in range(n, -1, -1):
    for j in range(i+1, n+1):
        dp[i][j] = max(a[i]-dp[i+1][j], a[j]-dp[i][j-1])
print(dp[0][n])
