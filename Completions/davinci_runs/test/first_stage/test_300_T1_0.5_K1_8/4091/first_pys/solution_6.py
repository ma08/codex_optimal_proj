


def solve(n, k, a):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i - 1]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j > i:
                continue
            dp[i][j] = dp[i - 1][j]
            for l in range(j - 1, i):
                dp[i][j] = max(dp[i][j], dp[l][j - 1] + s[i] - s[l])
    return dp[n][k]


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))


if __name__ == '__main__':
    main()