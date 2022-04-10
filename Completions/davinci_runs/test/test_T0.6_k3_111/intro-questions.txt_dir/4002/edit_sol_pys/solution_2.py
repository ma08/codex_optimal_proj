
def solve(n, m, k, matrix):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0] = [0] * (m + 1)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if j <= (m // 2):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1] + matrix[i - 1][j - 1] - k)
            else:
                dp[i][j] = dp[i][j - 1]
    return dp[-1][-1]


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, k, matrix))
