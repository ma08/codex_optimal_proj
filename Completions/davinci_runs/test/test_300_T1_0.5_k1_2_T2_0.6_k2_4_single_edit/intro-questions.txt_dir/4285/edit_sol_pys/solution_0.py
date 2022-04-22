

def solve(n, s):
    """
    >>> solve(7, '???abc')
    21
    >>> solve(7, 'a?b?c?')
    56
    """
    if n % 3 != 0:
        return 0
    mod = int(1e9 + 7)
    # dp[i][j] : number of subsequences ending at index i with character j
    dp = [[0] * 3 for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(3):
            if s[i] == '?':
                for k in range(3):
                    dp[i][k] += dp[i - 1][j]
            elif 'a' <= s[i] <= 'c':
                dp[i][ord(s[i]) - ord('a')] += dp[i - 1][j]
        for j in range(3):
            dp[i][j] %= mod
    return sum(dp[-1]) % mod


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(solve(n, s))
