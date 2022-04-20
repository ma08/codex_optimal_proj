def solve(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(0, len(s)):
        for j in range(0, len(t)):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            elif dp[i][j + 1] > dp[i + 1][j]:
                dp[i + 1][j + 1] = dp[i][j + 1]
            else:
                dp[i + 1][j + 1] = dp[i + 1][j]
    return dp[-1][-1]

s = input()
t = input()
print(solve(s, t))
