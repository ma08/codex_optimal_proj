def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j] + h[i - 1]
            if i > 1 and j > 1:
                dp[i][j] = max(dp[i][j], dp[i - 2][j - 1])
    print(dp[n][k])


if __name__ == '__main__':
    main()
