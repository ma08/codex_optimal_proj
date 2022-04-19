

n,m,k = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

def max_sum(matrix,n,m):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + matrix[i-1][j-1]
    return dp[n][m]

print(max_sum(matrix,n,m,k))
