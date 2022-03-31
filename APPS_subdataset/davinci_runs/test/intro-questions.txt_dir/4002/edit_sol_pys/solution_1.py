

def solve(n, m, k, matrix, dp):
    if dp[n][m] != -1:
        return dp[n][m]
    if n == 0:
        dp[n][m] = matrix[n][m]
    else:
        dp[n][m] = max(solve(n - 1, m, k, matrix, dp), solve(n - 1, m - 1, k, matrix, dp)) + matrix[n][m]
    return dp[n][m]


def main():
    n, m, k = [int(x) for x in input().split()]
    matrix = [[int(x) for x in input().split()] for i in range(n)]
    dp = [[-1 for i in range(m)] for j in range(n)]
    print(solve(n - 1, m - 1, k, matrix, dp) % k)


if __name__ == '__main__':
    main()
