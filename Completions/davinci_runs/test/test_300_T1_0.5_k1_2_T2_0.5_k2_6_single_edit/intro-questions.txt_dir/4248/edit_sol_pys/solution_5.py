
import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

dp = [0 for _ in range(n)]
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(n):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i])

print(dp[-1])
