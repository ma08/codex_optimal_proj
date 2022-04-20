

def solve(s, t):
    """
    >>> solve('bbaba', 'bb')
    3
    >>> solve('baaba', 'ab')
    2
    >>> solve('abcde', 'abcde')
    0
    >>> solve('asdfasdf', 'fasd')
    3
    """
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if s[i] == t[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return n - dp[0][0]


if __name__ == '__main__':
    s = input()
    t = input()
    print(solve(s, t))