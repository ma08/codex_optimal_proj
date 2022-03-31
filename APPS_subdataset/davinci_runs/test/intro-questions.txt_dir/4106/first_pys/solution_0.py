


def solve(n, k, x, a):
    """
    >>> solve(5, 2, 3, [5, 1, 3, 10, 1])
    18
    >>> solve(6, 1, 5, [10, 30, 30, 70, 10, 10])
    -1
    >>> solve(4, 3, 1, [1, 100, 1, 1])
    100
    """
    if x < k:
        return -1
    if k == 1:
        return sum(a)
    if k == n:
        return max(a)
    if k == n - 1:
        return max(a[0] + a[-1], sum(a) - a[1])
    if k == n - 2:
        return max(a[0] + a[-1], a[1] + a[-2], sum(a) - a[1] - a[2])
    if x == k:
        return sum(a[:k])

    # x > k
    dp = [0] * (k + 1)
    dp[0] = a[0]
    dp[1] = a[0] + a[1]
    dp[2] = a[0] + a[2]
    for i in range(3, k):
        dp[i] = max(dp[i - 1], dp[i - 2], dp[i - 3]) + a[i]
    return max(dp[k - 1], dp[k - 2], dp[k - 3]) + sum(a[k:x])


if __name__ == "__main__":
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, x, a))