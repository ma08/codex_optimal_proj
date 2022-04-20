

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

    s_len, t_len = len(s), len(t)
    dp = [[0] * (t_len + 1) for _ in range(s_len + 1)]

    for i in range(1, s_len + 1):
        for j in range(1, t_len + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return s_len - dp[-1][-1]


if __name__ == "__main__":
    s = input()
    t = input()
    print(solve(s, t))