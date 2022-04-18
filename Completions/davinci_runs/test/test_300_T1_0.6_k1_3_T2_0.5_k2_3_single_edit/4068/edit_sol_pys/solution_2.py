import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))

a.sort()
dp = [0] * n
dp[0] = a[0]

for i in range(1, n):
    if a[i] - dp[i - 1] > 1:
        dp[i] = dp[i - 1] + 1
    elif a[i] - dp[i - 1] == 1:
        dp[i] = dp[i - 1] + 2
    else:
        dp[i] = dp[i - 1]

print(dp[-1])
