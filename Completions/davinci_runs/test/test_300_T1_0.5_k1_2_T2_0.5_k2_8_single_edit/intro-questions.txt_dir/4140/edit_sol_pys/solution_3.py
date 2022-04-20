

from sys import stdin

s = stdin.readline().strip() + '0'

# we can solve this problem by dynamic programming
# dp[i][j] is the number of ways to make a string of length i
# that ends with the letter j
# dp[i][j] = sum(dp[i - 1][k]) for k not equal to j
# dp[0][0] = 1

dp = [[0 for _ in range(26)] for _ in range(len(s))]

dp[0][0] = 1

for i in range(1, len(s)):
    for j in range(26):
        for k in range(26):
            if j != k:
                dp[i][j] += dp[i - 1][k]

ans = 0
for i in range(26):
    ans += dp[len(s) - 1][i]

print(ans)
