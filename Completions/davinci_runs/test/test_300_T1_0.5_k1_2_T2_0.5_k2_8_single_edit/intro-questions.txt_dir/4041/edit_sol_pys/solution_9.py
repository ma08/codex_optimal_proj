

s = "abcdefghijklmnopqrstuvwxyz"
t = "abcdefghijklmnopqrstuvwxyz"

def get_lcs(s,t):
    # Create a matrix to store results of subproblems
    dp = [[0] * (len(s) + 1) for i in range(len(t) + 1)]

    # Fill d[][] in bottom up manner
    for i in range(len(t) + 1):
        for j in range(len(s) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif t[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(t)][len(s)]


print(len(s) - get_lcs(s,t))
