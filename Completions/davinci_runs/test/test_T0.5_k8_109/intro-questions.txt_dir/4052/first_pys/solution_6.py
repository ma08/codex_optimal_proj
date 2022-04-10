

def solve(n, s, t):
    """
    >>> solve(6, "abcdef", "abdfec")
    '4\\n3 5 4 5 '
    >>> solve(4, "abcd", "accd")
    '-1'
    """

    # # brute force
    # # O(n * 2^n)
    # # dp[s] = min(dp[s], dp[s[:i] + s[i+1:j] + s[i] + s[j+1:]] + 1)
    # # dp[s] = min(dp[s], dp[s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]] + 1)
    # dp = {s : 0}
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         for s in dp.keys():
    #             if s[i] != s[j]:
    #                 dp[s[:i] + s[i+1:j] + s[i] + s[j+1:]] = min(dp.get(s[:i] + s[i+1:j] + s[i] + s[j+1:], float('inf')), dp[s] + 1)
    #                 dp[s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]] = min(dp.get(s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:], float('inf')), dp[s] + 1)
    # if t not in dp:
    #     return '-1'
    # return '{}\\n{}'.format(dp[t], ' '.join(map(str, [i for i in range(n - 1) if dp[s[:i] + s[i+1:]] + 1 == dp[t]])))

    # O(n)
    # 1. find the first mismatch
    # 2. find the first match after mismatch
    # 3. swap
    # 4. repeat 1-3 until all matches
    # 5. swap the rest
    i = 0
    while i < n:
        if s[i] == t[i]:
            i += 1
        else:
            break
    j = i
    while j < n:
        if s[j] == t[j]:
            j += 1
        else:
            break
    if j == n:
        return '-1'
    if j == n - 1:
        return '1\\n{}'.format(i)
    if j == i + 1:
        return '2\\n{} {}'.format(i, j)
    return '{}\\n{} {} {}'.format(j - i, i, j, j)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # n = int(raw_input())
    # s = raw_input()
    # t = raw_input()
    # print solve(n, s, t)