

def solve_dp(n, h, l, r, a):
    dp = [[0] * h for i in range(n)]
    for i in range(n):
        for j in range(h):
            if dp[i][j] == 0:
                continue
            if (j + a[i]) % h >= l and (j + a[i]) % h <= r:
                dp[i][(j + a[i]) % h] = max(dp[i][(j + a[i]) % h], dp[i - 1][j] + 1)
            if (j + a[i] - 1) % h >= l and (j + a[i] - 1) % h <= r:
                dp[i][(j + a[i] - 1) % h] = max(dp[i][(j + a[i] - 1) % h], dp[i - 1][j] + 1)
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
    return max(dp[n - 1])


n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))
print(solve_dp(n, h, l, r, a))
