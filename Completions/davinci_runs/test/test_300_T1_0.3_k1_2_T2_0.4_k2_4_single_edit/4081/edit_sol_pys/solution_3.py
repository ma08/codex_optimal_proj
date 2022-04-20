


def solve(n, a):
    a = [0] + a
    dp = [[0, 0] for _ in range(n + 1)]
    dp[1][0] = 1
    dp[1][1] = 1
    for i in range(2, n + 1):
        if a[i] > a[i - 1]:
            dp[i][0] = dp[i - 1][0] + 1
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0])
        else:
            dp[i][0] = 1
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0])
    return max(dp[-1])


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))


if __name__ == "__main__":
    main()
