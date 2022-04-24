
import math

def solve(n, m, k, A):
    # dp[i][j] = max sum of first i rows, with j columns chosen, remainder is j
    dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for r in range(k + 1):
                if j <= m // 2:
                    dp[i][j][r] = max(dp[i][j - 1][r], dp[i - 1][j][r], dp[i - 1][j - 1][(A[i - 1][j - 1] + r) % k] + A[i - 1][j - 1])
                else:
                    dp[i][j][r] = dp[i][j - 1][r]

    return dp[n][m // 2][0] // k * k


def main():
    n, m, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]

    print(solve(n, m, k, A))


if __name__ == '__main__':
    main()
