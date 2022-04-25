

n,m = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))


def max_sum(matrix,n,m):
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = matrix[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + matrix[i][j]
    return dp[n - 1][m - 1]


print(max_sum(matrix, n, m))
