
n,m,k = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

def max_sum(matrix,n,m,k):
    dp = [[0 for i in range(m)] for j in range(n)]
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + matrix[i][j]
    return dp[n][m]

print(max_sum(matrix,n,m,k))
