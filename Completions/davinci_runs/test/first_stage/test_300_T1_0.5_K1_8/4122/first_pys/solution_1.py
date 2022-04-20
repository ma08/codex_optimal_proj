

H, n = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

if H < 0:
    print(0)
    exit(0)

# dp[i] = the number of rounds after which the monster is dead
dp = [0 for _ in range(n)]
dp[0] = d[0]
for i in range(1, n):
    dp[i] = max(dp[i - 1] + d[i], d[i])

if dp[-1] < 0:
    print(-1)
else:
    print(H // dp[-1] * n + (H % dp[-1] - 1) // d[-1] + 1)