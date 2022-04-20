
n,m,k = map(int, input().split())
matrix = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input().split()))

def max_sum(matrix,n,m,k):
    dp = [[0 for i in range(m)] for j in range(k)]
    for i in range(n):
        for j in range(m):
            dp[0][j] = matrix[i][j]
    for i in range(1,k):
        for j in range(m):
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + matrix[i][j]
    return dp[k-1][m-1]

print(max_sum(matrix,n,m,k))
