
#

def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n] % 1000000007)


if __name__ == '__main__':
    main()
