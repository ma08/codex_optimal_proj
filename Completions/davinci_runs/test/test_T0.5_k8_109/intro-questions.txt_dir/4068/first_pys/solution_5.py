

# N: int
# M: int
# a: list[int]
N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]

# dp[i]: int
#   i: int
#     0 <= i <= N
dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, N + 1):
    # dp[i] = dp[i - 1] + dp[i - 2]
    # - if i is not in a
    if i not in a:
        dp[i] = dp[i - 1] + dp[i - 2]
    else:
        # dp[i] = 0
        # - if i is in a
        dp[i] = 0
    dp[i] %= 10 ** 9 + 7

print(dp[N])