

def solve_dp(n, h, l, r, a, dp):
    if n == 0:
        return 0
    if dp[n][h][l][r] != -1:
        return dp[n][h][l][r]
    if (h + a[n - 1]) % h >= l and (h + a[n - 1]) % h <= r:
        dp[n][h][l][r] = max(dp[n][h][l][r], solve_dp(n - 1, (h + a[n - 1]) % h, l, r, a, dp) + 1)
    if (h + a[n - 1] - 1) % h >= l and (h + a[n - 1] - 1) % h <= r:
        dp[n][h][l][r] = max(dp[n][h][l][r], solve_dp(n - 1, (h + a[n - 1] - 1) % h, l, r, a, dp) + 1)
    return dp[n][h][l][r]


n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))
dp = [[[[-1] * (r + 1) for j in range(l + 1)] for k in range(h + 1)] for l in range(n + 1)]
print(solve_dp(n, 0, l, r, a, dp))
