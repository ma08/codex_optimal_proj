
def solve_dp(n, h, l, r, a):
    dp = [[0] * h for _ in range(n)]
    dp[0][a[0]] = 1
    for i in range(1, n):
        for j in range(h):
            if dp[i - 1][j] == 0:
                continue
            if (j + a[i]) % h >= l and (j + a[i]) % h <= r:
                dp[i][(j + a[i]) % h] = max(dp[i][(j + a[i]) % h], dp[i - 1][j] + 1)
            if (j + a[i] - 1) % h >= l and (j + a[i] - 1) % h <= r:
                dp[i][(j + a[i] - 1) % h] = max(dp[i][(j + a[i] - 1) % h], dp[i - 1][j] + 1)
    return max(dp[n - 1])



n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))
print(solve_dp(n, h, l, r, a))
