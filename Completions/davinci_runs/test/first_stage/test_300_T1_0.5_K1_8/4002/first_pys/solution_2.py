


def solve(n, m, k, matrix):
    """
    >>> solve(3, 4, 3, [[1, 2, 3, 4], [5, 2, 2, 2], [7, 1, 1, 4]])
    24
    >>> solve(5, 5, 4, [[1, 2, 4, 2, 1], [3, 5, 1, 2, 4], [1, 5, 7, 1, 2], [3, 8, 7, 1, 2], [8, 4, 7, 1, 6]])
    56
    """
    dp = [[0 for _ in range(k)] for _ in range(m + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for l in range(k):
                dp[j][(l + matrix[i - 1][j - 1]) % k] = max(dp[j - 1][l], dp[j][(l + matrix[i - 1][j - 1]) % k])
    return dp[m][0]


def main():
    n, m, k = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solve(n, m, k, matrix))


if __name__ == '__main__':
    main()