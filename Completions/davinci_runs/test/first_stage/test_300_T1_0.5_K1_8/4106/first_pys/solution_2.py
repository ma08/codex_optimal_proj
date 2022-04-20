

def solve(n, k, x, a):
    """
    >>> solve(5, 2, 3, [5, 1, 3, 10, 1])
    18
    >>> solve(6, 1, 5, [10, 30, 30, 70, 10, 10])
    -1
    >>> solve(4, 3, 1, [1, 100, 1, 1])
    100
    """
    if x < n - k + 1:
        return -1
    if n == x:
        return sum(a)
    # k <= n - k + 1 <= x
    # a = [5, 1, 3, 10, 1]
    # k = 2
    # x = 3
    # n = 5
    # dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - k] + a[j])
    dp = [[0] * (n + 1) for _ in range(x + 1)]
    for i in range(1, x + 1):
        for j in range(1, n + 1):
            if i == 1:
                dp[i][j] = dp[i][j - 1] + a[j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][max(j - k, 0)] + a[j - 1])
    return dp[x][n]


if __name__ == '__main__':
    n, k, x = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    print(solve(n, k, x, a))