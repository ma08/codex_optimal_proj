

import sys

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0 for j in range(x + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, x + 1):
        if i < k:
            dp[i][j] = max(dp[i - 1][j], a[i - 1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - k][j - 1] + a[i - 1])

print(dp[n][x])