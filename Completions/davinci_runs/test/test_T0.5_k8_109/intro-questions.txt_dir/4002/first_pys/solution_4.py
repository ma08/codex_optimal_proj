

def sub_matrix_sum(matrix, k):
    n = len(matrix)
    m = len(matrix[0])
    dp = [[[0 for _ in range(k)] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for r in range(k):
                dp[i][j][r] = max(dp[i][j][r], dp[i][j - 1][r])
                if j - 1 >= 0:
                    dp[i][j][(r + matrix[i][j]) % k] = max(dp[i][j][(r + matrix[i][j]) % k], dp[i][j - 1][r] + matrix[i][j])
                if i - 1 >= 0:
                    dp[i][j][r] = max(dp[i][j][r], dp[i - 1][j][r])
                    dp[i][j][(r + matrix[i][j]) % k] = max(dp[i][j][(r + matrix[i][j]) % k], dp[i - 1][j][r] + matrix[i][j])
    return dp[n - 1][m - 1][0]


def main():
    n, m, k = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(sub_matrix_sum(matrix, k))


if __name__ == '__main__':
    main()