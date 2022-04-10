

# Read input
N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]

# Initialize
dp = [0] * N
dp[0] = 1

# DP
for i in range(N):
    if i + 1 < N and (i + 1) not in a:
        dp[i + 1] += dp[i]
    if i + 2 < N and (i + 2) not in a:
        dp[i + 2] += dp[i]

# Output
print(dp[-1] % (10**9 + 7))