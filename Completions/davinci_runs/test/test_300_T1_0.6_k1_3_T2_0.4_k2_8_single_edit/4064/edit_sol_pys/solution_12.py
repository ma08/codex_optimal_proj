

def solve_dp(n, k, h, l, r, a):
    dp = [[[0] * h for i in range(k + 1)] for j in range(n)]
    dp[0][0][a[0]] = 1
    for i in range(n - 1):
        for j in range(k + 1):
            for t in range(h):
                if dp[i][j][t] == 0:
                    continue
                if (t + a[i + 1]) % h >= l and (t + a[i + 1]) % h <= r:
                    dp[i + 1][j][(t + a[i + 1]) % h] = max(dp[i + 1][j][(t + a[i + 1]) % h], dp[i][j][t] + 1)
                if j < k and (t + a[i + 1] - 1) % h >= l and (t + a[i + 1] - 1) % h <= r:
                    dp[i + 1][j + 1][(t + a[i + 1] - 1) % h] = max(dp[i + 1][j + 1][(t + a[i + 1] - 1) % h], dp[i][j][t] + 1)
    return max([max(dp[n - 1][k]) for k in range(k + 1)])


n, k, h, l, r = map(int, input().split())
a = list(map(int, input().split()))
print(solve_dp(n, h, l, r, a))
