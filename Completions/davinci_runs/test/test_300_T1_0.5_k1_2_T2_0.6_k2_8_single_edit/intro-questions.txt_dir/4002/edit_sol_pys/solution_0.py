

n,m,k = map(int, input().split())
# fill the matrix
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

def max_sum(matrix,n,m,k):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n):
        for j in range(m):
            if j == 1:
                dp[i][j] = dp[i-1][j] + matrix[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + matrix[i-1][j-1]
    return dp[n][m]

print(max_sum(matrix,n,m,k))
