import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n)]
dp[0] = a[0]
dp[1] = max(a[0]+a[1], a[1])
dp[2] = max(a[0]+a[2], a[1]+a[2])
for i in range(3, n):
    dp[i] = max(dp[i-3]+a[i-1]+a[i], dp[i-2]+a[i])
print(dp[n-1])
