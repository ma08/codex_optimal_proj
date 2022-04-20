


def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [[0] * (x + 1) for _ in range(n)]

    dp[0][1] = a[0]
    dp[1][1] = max(dp[0][1], a[1])

    for i in range(2, n):
        for j in range(1, x + 1):
            dp[i][j] = dp[i - 1][j]
            for p in range(max(0, i - k), i):
                dp[i][j] = max(dp[i][j], dp[p][j - 1] + sum(a[p:i + 1]))

    if dp[-1][x] > 0:
        print(dp[-1][x])
    else:
        print(-1)


if __name__ == "__main__":
    main()