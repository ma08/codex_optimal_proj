


def main():
    n, k = map(int, input().split())
    dp = [0] * (k + 1)
    dp[k] = 1.0
    for i in range(k - 1, 0, -1):
        dp[i] = dp[i + 1] * (n - 1) / n + (dp[i + 1] + dp[i + 2]) / 2 / n
    print(dp[1])  # dp[1] = 1/n * (dp[2] + 2*dp[3])


if __name__ == '__main__':
    main()
