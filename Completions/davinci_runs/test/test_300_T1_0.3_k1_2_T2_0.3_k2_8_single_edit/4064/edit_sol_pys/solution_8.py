
n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0] * h for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(h):
        if dp[i - 1][j]:
            dp[i][(j + a[i - 1]) % h] = 1
            dp[i][(j + a[i - 1] - 1) % h] = 1

print(sum(dp[l:r + 1]))
