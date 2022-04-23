

# n, k = map(int, input().split())  # n, k = 5, 2
# a = list(map(int, input().split()))  # a = [1, 2, 15, 15, 15]
n, k = 6, 1  # n, k = 6, 1
a = [36, 4, 1, 25, 9, 16]  # a = [36, 4, 1, 25, 9, 16]
# n, k = 4, 4  # n, k = 4, 4
# a = [1, 10, 100, 1000]  # a = [1, 10, 100, 1000]


def max_consecutive_subarray(a, n):
    """
    Find the maximum number of consecutive elements in the array.

    :param a: array of integers
    :return: the maximum number of consecutive elements in the array
    """
    max_len = 0
    curr_len = 0
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) <= 5:
            curr_len += 1
        else:
            max_len = max(max_len, curr_len)
            curr_len = 0
    return max(max_len, curr_len)
    """
    Find the maximum number of consecutive elements in the array with at most k changes.

    :param a: array of integers
    :param k: number of changes
    :return: the maximum number of consecutive elements in the array with at most k changes
    """


def solve(a, k):
    a.sort()
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j]
            max_len = max_consecutive_subarray(a[:i], i)
            dp[i][j] = max(dp[i][j], dp[i - max_len][j - 1] + max_len)
    return dp[n][k]


print(solve(a, k))
