
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# https://atcoder.jp/contests/abc097/tasks/arc097_a
def solve(n, s):
    """
    >>> solve(6, 'ac?bc')
    24
    >>> solve(7, '???????')
    2835
    >>> solve(9, 'cccbbbaa')
    0
    1
    >>> solve(5, 'a???c')  # 'aaabc', 'aabac', 'aabca', 'ababc', 'abaca', 'abcac'
    6
    >>> solve(5, '?a??c')  # 'caaac', 'caaca', 'caacc', 'cbaac', 'cbaca', 'cbacc'
    6
    >>> solve(5, '??a?c')  # 'ccaac', 'ccaac', 'ccaac', 'ccaac', 'ccaac', 'ccaac'
    6
    """
    mod = int(1e9 + 7)
    # dp[i][j] : number of subsequences ending at index i with character j
    dp = [[0] * 3 for _ in range(n + 1)]  # dp[i][j] : number of subsequences ending at index i with character j
    dp[0][0] = 1
    # dp[i][j] = dp[i - 1][j] + dp[i - 1][k] for k in range(3)
    for i in range(1, n + 1):
        for j in range(3):
            if s[i - 1] == '?':
                dp[i][j] = sum(dp[i - 1])
            elif 'a' <= s[i - 1] <= 'c':
                dp[i][ord(s[i - 1]) - ord('a')] = dp[i - 1][j]
        for j in range(3):
            dp[i][j] %= mod
    return sum(dp[n]) % mod


if __name__ == '__main__':
    n = int(readline())
    s = readline().decode()
    print(solve(n, s))
