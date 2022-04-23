
# https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/the-great-kian/
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
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1],dp[i-1][(j+1)%m]) + matrix[i][j]
    return dp[n-1][m-1]

print(max_sum(matrix,n,m,k))
