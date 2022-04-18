
def solve(n, m, k, A):
    # dp[i][j] = max sum of first i rows, with j columns chosen
    dp = [[0] * (m // 2 + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m // 2 + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1] + A[i - 1][j - 1])

    return dp[n][m // 2] // k * k


def main():
    n, m, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]

    print(solve(n, m, k, A))


if __name__ == '__main__':
    main()
