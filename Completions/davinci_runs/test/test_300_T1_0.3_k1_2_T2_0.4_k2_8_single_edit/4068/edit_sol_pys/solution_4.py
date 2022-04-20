


def main():
    n, m = map(int, input().split())
    a = set([int(input()) for _ in range(m)])
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(2, n + 1):
        if i not in a:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    print(dp[n] % 1000000007)


if __name__ == '__main__':
    main()
