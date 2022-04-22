

n,m,k = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

def max_sum(matrix,n,m,k):
    dp = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = matrix[i][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + matrix[i][j]
    return dp[n-1][m-1]
<<<<<<< HEAD

=======
print(max_sum(matrix,n,m,k))
>>>>>>> 9d7b0c8d3b3e1c3fc1d7e589f8c0f7b56d6b74d0
print(max_sum(matrix,n,m,k))
