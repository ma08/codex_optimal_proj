

n = int(input())
h = list(map(int, input().split()))

# dp[i] = max(dp[i-1], dp[i-2]+1)
dp = [0]*n
dp[0] = 0
dp[1] = 1 if h[1] > h[0] else 0

for i in range(2, n):
    if h[i] > h[i-1]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]

print(dp[-1])