import sys
sys.setrecursionlimit(10**7)

n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0 for i in range(h)] for j in range(n)]

dp[0][a[0]] = 1

for i in range(1, n):
    for j in range(h):
        if j - a[i] > l and j - a[i] < r:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i]] + 1)
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i]])

print(max(dp[n - 1][0], dp[n - 1][1]))
