

#!/bin/python3

import sys

def solve(s, t):
    # Complete this function
    # dp[i][j] = max substring length that can be removed such that s[:i] and t[:j] are subsequences
    # dp[i][j] = dp[i-1][j] if s[i] != t[j]
    # else dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + 1)
    dp = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i-1] != t[j-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + 1)
    return len(s) - dp[len(s)][len(t)]

s = input().strip()
t = input().strip()
result = solve(s, t)
print(result)