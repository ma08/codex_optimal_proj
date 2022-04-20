

def subsequence(s, t):
    """ Returns the maximum length of a substring of s that can be removed
    so that t remains a subsequence of s. """
    # We use dynamic programming. Our state is (i, j), where i is the index
    # of the character in s and j is the index of the character in t. We
    # want to know the longest substring that can be removed from s[:i] so
    # that t[:j] is a subsequence of s[:i].
    #
    # We can make the transition by considering whether s[i] == t[j]. If so,
    # then we need to remove a substring from s[:i-1] so that t[:j-1] is a
    # subsequence of s[:i-1]. If not, then we need to remove a substring from
    # s[:i-1] so that t[:j] is a subsequence of s[:i-1].
    #
    # The base case is when i == 0, in which case we can remove the entire
    # substring s[:i] and t[:j] is a subsequence.
    #
    # The answer is the maximum value of dp[i][j] over all i and j.
    n = len(s)
    m = len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
    return dp[n][m]

print(subsequence(input(), input()))