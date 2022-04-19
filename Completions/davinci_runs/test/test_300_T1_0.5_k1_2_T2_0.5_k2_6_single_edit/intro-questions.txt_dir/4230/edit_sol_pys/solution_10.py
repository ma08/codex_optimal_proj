n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if a[i] == b[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
print(dp[n][n])
