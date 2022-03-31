

N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]

mod = 10 ** 9 + 7

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, N + 1):
    if i in A:
        continue
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= mod

print(dp[N])