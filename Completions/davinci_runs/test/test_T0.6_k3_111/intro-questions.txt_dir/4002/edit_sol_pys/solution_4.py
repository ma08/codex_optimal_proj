
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j] = max sum of the first j elements of the ith row
dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if j == 0:
            dp[i][j] = matrix[i][j]
        else:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + matrix[i][j])

# dp2[i][j] = max sum of the first i rows, ending with the jth element of the ith row
dp2 = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0:
            dp2[i][j] = dp[i][j]
        else:
            for k in range(j+1):
                dp2[i][j] = max(dp2[i][j], dp2[i-1][k] + dp[i][j])

print(max(dp2[-1]))
