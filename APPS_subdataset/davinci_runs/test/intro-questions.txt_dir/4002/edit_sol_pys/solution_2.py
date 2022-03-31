# https://atcoder.jp/contests/abc094/tasks/arc095_a


def main():
    n, m, k = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])

    dp = [[0] * (k+1) for i in range(n+1)]
    for i in range(n):
        for j in range(k+1):
            dp[i][j] = dp[i-1][j]

        for j in range(m+1):
            for l in range(k):
                dp[i][(l+a[i][j]) % k] = max(dp[i][(l+a[i][j]) % k], dp[i-1][l] + a[i][j])

    print(dp[n-1][0])


if __name__ == "__main__":
    main()
