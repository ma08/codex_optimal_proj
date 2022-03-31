
def solve(n, m, k, matrix):
    dp = [[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        dp[0][i] = matrix[0][i]
    for i in range(1, n):
        for j in range(m):
            for k in range(j + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + matrix[i][j])
    return dp[n - 1][m - 1] % k


def main():
    n, m, k = [int(x) for x in input().split()]
    matrix = [[int(x) for x in input().split()] for i in range(n)]
    print(solve(n, m, k, matrix))


if __name__ == '__main__':
    main()
