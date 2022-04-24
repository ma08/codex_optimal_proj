

    # n, m, k = map(int, input().split())
    # matrix = []
    # for _ in range(n):
    #     matrix.append(list(map(int, input().split())))
    # dp = [[0 for i in range(k)] for j in range(m + 1)]
    # for i in range(1, m + 1):
    #     for j in range(k):
    #         for r in range(n):
    #             dp[i][j] = max(dp[i][j], dp[i - 1][j] + matrix[r][i - 1])
    #             dp[i][(j - matrix[r][i - 1]) % k] = max(dp[i][(j - matrix[r][i - 1]) % k], dp[i - 1][j] + matrix[r][i - 1])
    # print(max(dp[m][0], dp[m][k // 2]))
def main():
    n, m, k = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    dp = [[0 for i in range(k + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        for j in range(k + 1):
            for r in range(1, n + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + matrix[r - 1][i - 1])
                dp[i][j] = max(dp[i][j], dp[i - 1][(j - matrix[r - 1][i - 1]) % k] + matrix[r - 1][i - 1])
    print(dp[m][k // 2])

if __name__ == "__main__":
    main()
