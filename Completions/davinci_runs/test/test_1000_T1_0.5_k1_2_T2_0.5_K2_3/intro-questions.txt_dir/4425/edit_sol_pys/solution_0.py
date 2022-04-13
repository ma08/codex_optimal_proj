
def main():
    n, k = map(int, input().split())
    dp = [0] * (k+1)
    dp[k] = 1
    for i in range(k-1, 0, -1):
        dp[i] = dp[i+1] * (n-1) / n + (dp[i+1] + dp[i+2]) / 2
    print(dp[1] / n)


if __name__ == '__main__':
    main()
