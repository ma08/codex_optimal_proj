

n, k = [int(i) for i in input().split()]
s = input()

dp = [[-1 for i in range(k+1)] for j in range(n+1)]

for i in range(n+1):
    dp[i][0] = 0

for i in range(1, n+1):
    for j in range(1, k+1):
        dp[i][j] = dp[i-1][j]
        for x in range(i-1, -1, -1):
            if dp[x][j-1] != -1:
                dp[i][j] = min(dp[i][j], dp[x][j-1] + (i-x-1))

if dp[n][k] == -1:
    print(-1)
else:
    print(dp[n][k])