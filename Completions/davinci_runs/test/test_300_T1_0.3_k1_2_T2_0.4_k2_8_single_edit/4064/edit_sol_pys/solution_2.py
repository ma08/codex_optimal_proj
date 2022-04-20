
n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0] * h for _ in range(n)]
dp[0][0] = 1

for i in range(1, n):
    for j in range(h):
        if dp[i - 1][j]:
            dp[i][(j + a[i]) % h] = 1
            dp[i][(j + a[i] - 1) % h] = 1

print(sum(dp[-1][l:r + 1]))
