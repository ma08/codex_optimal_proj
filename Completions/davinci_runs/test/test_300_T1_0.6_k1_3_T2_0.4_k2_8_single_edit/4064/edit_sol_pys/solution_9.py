import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split())) + [0]
b = list(map(int, input().split())) + [0]

dp = [[0, 0] for i in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + a[i])
    dp[i][1] = max(dp[i - 1][0] + b[i], dp[i - 1][1])

print(max(dp[n - 1][0], dp[n - 1][1]))
