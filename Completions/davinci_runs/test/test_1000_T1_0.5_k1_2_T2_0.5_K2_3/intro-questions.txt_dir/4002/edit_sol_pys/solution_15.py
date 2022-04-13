
n,m,k = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

def max_sum(matrix,n,m,k):
    dp = [[0 for i in range(m+1)] for i in range(n+1)]
    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = matrix[i][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + matrix[i][j] - k
    return dp[n][m]

print(max_sum(matrix,n,m,k))
