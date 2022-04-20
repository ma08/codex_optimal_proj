import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * 100001
dp[0] = 1
for i in range(n):
    for j in range(1, m + 1):
        if arr[i] <= j:
            dp[j] += dp[j - arr[i]]

print(dp[m])
