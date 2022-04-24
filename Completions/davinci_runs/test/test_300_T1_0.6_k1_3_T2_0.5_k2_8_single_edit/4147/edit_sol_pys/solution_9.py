

n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]

# dp[i][j][k] = min(mp) to obtain bamboos with lengths of a, b, c from l[0:i]
# dp[i][j][k] = min(dp[i-1][j][k], dp[i-1][j-1][k-1] + 10, dp[i-1][j-1][k] + 1, dp[i-1][j-1][k] + 1)
dp = [[[float("inf") for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
dp[0][0][0] = 0
for i in range(n):
    for j in range(i+1):
        for k in range(j+1):
            if l[i] == a and j == 0:
                dp[i+1][j+1][k] = min(dp[i+1][j+1][k], dp[i][j][k])
            if l[i] == b and k == 0:
                dp[i+1][j][k+1] = min(dp[i+1][j][k+1], dp[i][j][k])
            if l[i] == c and k == j:
                dp[i+1][j][k+1] = min(dp[i+1][j][k+1], dp[i][j][k])
            if j > 0 and k > 0 and l[i] + a <= 1000:
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j-1][k-1]+10)
            if j > 0 and k > 0 and l[i] + b <= 1000:
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j-1][k-1]+10)
            if j > 0 and k > 0 and l[i] + c <= 1000:
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j-1][k-1]+10)
            if j > 0 and l[i] + 1 <= 1000:
                dp[i+1][j+1][k] = min(dp[i+1][j+1][k], dp[i][j][k]+1)
            if j > 0 and l[i] - 1 >= 1:
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k]+1)

print(dp[n][1][1] if dp[n][1][1] != float("inf") else -1)
