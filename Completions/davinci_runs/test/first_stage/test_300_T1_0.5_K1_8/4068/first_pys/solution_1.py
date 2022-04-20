


def main():
    n, m = map(int, input().split())
    a = set(map(int, [input() for _ in range(m)]))
    dp = [1] + [0] * (n)
    for i in range(n):
        if i + 1 not in a:
            dp[i + 1] += dp[i]
        if i + 2 not in a:
            dp[i + 2] += dp[i]
    print(dp[-1] % 1000000007)


if __name__ == '__main__':
    main()