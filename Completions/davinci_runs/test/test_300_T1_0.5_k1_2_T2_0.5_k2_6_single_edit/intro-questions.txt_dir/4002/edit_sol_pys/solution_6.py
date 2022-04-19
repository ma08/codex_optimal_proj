
n,m,k = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

def max_sum(matrix, n, m, k):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n-1):
        for j in range(m-1):
            if i == 0:
                dp[i][j] = matrix[i][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + matrix[i][j]
    return dp[n-1][m-1]

print(max_sum(matrix,n,m,k))
