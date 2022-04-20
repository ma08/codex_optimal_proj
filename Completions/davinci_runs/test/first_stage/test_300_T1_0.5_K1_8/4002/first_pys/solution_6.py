

def main():
    n, m, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    # dp[i][j][k] = the maximum sum divisible by k that can be obtained from the first i rows
    # where the first j columns are used in the first i rows
    dp = [[[0 for _ in range(k)] for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for p in range(k):
                dp[i][j][p] = max(dp[i][j][p], dp[i][j - 1][p])
                if j <= (m + 1) // 2:
                    dp[i][j][(p + matrix[i - 1][j - 1]) % k] = max(dp[i][j][(p + matrix[i - 1][j - 1]) % k], dp[i][j - 1][p] + matrix[i - 1][j - 1])
            for p in range(k):
                dp[i][j][p] = max(dp[i][j][p], dp[i - 1][j][p])

    ans = max(dp[n][m])
    print(ans)

if __name__ == "__main__":
    main()