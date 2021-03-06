
import sys
input = sys.stdin.readline

def solve(s, t):
    n = len(s) + 1
    m = len(t) + 1
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = i
    for j in range(m):
        dp[0][j] = j
    for i in range(1, n):
        for j in range(1, m):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else: 
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
    return dp[-1][-1]

s = input().rstrip()
t = input().rstrip()
print(solve(s, t))
