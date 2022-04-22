

def solve(n, s):
    """
    >>> solve(3, 'abc')
    6
    >>> solve(6, 'acbacb')
    36
    """
    mod = int(1e9 + 7)
    # dp[i][j] : number of subsequences ending at index i with character j
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(3):
            if s[i - 1] == '?':
                for k in range(3):
                    dp[i][k] += dp[i - 1][j]
            elif 'a' <= s[i - 1] <= 'c':
                dp[i][ord(s[i - 1]) - ord('a')] += dp[i - 1][j]
        for j in range(3):
            dp[i][j] %= mod
    return sum(dp[n]) % mod


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(solve(n, s))
