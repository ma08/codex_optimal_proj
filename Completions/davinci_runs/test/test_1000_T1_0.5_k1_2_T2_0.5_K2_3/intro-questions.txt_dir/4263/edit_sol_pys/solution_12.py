import sys
sys.setrecursionlimit(10 ** 7)

S = int(input())

dp = [0] * (S + 1)
dp[0] = 1

for i in range(1, S + 1):
    if i - 3 >= 0:
        dp[i] += dp[i - 3]
    if i - 7 >= 0:
        dp[i] += dp[i - 7]
    if i - 10 >= 0:
        dp[i] += dp[i - 10]

print(dp[S])
