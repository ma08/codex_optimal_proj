

def solve(s, t):
    """
    >>> solve("bbaba", "bb")
    3
    >>> solve("baaba", "ab")
    2
    >>> solve("abcde", "abcde")
    0
    >>> solve("asdfasdf", "fasd")
    3
    """
    n = len(s)
    m = len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return n - dp[n][m]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    s = input()
    t = input()
    print(solve(s, t))