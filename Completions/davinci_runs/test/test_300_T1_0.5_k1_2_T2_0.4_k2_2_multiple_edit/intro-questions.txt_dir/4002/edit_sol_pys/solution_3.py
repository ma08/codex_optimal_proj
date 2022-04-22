import sys

n,m,k = map(int, input().split())


if n == 0 or m == 0 or k == 0:
    print(0)
    sys.exit()
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

def max_sum(matrix,n,m):
    dp = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = matrix[i][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + matrix[i][j]
    return dp[n-1][m-1]

print(max_sum(matrix,n,m))
