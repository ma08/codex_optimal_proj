

def solve(n, m, k, matrix):
    # dp[i][j][b]: number of paths from (1, 1) to (i, j) with xor sum equal to b
    dp = [[[0 for b in range(1024)] for j in range(m)] for i in range(n)]
    dp[0][0][matrix[0][0]] = 1
    for i in range(n):
        for j in range(m):
            for b in range(1024):
                if i + 1 < n:
                    dp[i + 1][j][b ^ matrix[i + 1][j]] += dp[i][j][b]
                if j + 1 < m:
                    dp[i][j + 1][b ^ matrix[i][j + 1]] += dp[i][j][b]
    return dp[n - 1][m - 1][k]

n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]
print(solve(n, m, k, matrix))