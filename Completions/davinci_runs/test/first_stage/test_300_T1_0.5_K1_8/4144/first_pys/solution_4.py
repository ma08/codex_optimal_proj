

n = int(input())

mod = 10**9 + 7

# dp[i] = number of sequences of length i
dp = [0] * (n + 1)
dp[1] = 2
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] * 10 - dp[i - 2]) % mod
print(dp[n])