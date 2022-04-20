
def solve(s, t, n):
    # dp[i][j] = length of the longest common subsequence from first i chars of s and first j chars of t
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return n - dp[-1][-1]

s = input()
t = input()
print(solve(s, t, len(s)))
