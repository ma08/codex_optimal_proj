


def read_input():
    n, k = map(int, raw_input().split())
    s = raw_input()
    return n, k, s


def solve(n, k, s):
    # dp[i][j] means number of ways to form a set of size j using first i characters of s
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(k + 1):
            dp[i][j] = dp[i - 1][j]
            if j - i >= 0:
                dp[i][j] += dp[i - 1][j - i]
            if dp[i][j] > 10 ** 9 + 7:
                dp[i][j] -= 10 ** 9 + 7

    if dp[n][k] == 0:
        return -1
    ans = 0
    for i in range(1, n + 1):
        ans += (i * dp[i][k]) % (10 ** 9 + 7)
        ans %= (10 ** 9 + 7)
    return ans


def main():
    n, k, s = read_input()
    ans = solve(n, k, s)
    print ans


if __name__ == '__main__':
    main()