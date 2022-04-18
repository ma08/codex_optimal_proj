

def solve_dp(n, h, l, r, a, s):
    dp = [[0] * h for i in range(n)]
    dp[0][s[0]] = 1
    for i in range(n - 1):
        for j in range(h):
            if dp[i][j] == 0:
                continue
            if (j + s[i + 1]) % h >= l and (j + s[i + 1]) % h <= r:
                dp[i + 1][(j + s[i + 1]) % h] = max(dp[i + 1][(j + s[i + 1]) % h], dp[i][j] + 1)
            if (j + s[i + 1] - 1) % h >= l and (j + s[i + 1] - 1) % h <= r:
                dp[i + 1][(j + s[i + 1] - 1) % h] = max(dp[i + 1][(j + s[i + 1] - 1) % h], dp[i][j] + 1)
    return max(dp[n - 1])


n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))
s = [0]
for i in range(n - 1):
    s.append((s[i] + a[i]) % h)
print(solve_dp(n, h, l, r, a, s))
