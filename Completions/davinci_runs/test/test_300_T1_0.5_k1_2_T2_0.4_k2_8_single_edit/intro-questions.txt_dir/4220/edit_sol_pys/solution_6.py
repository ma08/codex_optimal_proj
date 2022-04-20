

N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [float('inf')] * N
dp[0] = 0

for i in range(N):
    for j in range(1, K+1):
        if i + j < N:
            dp[i+j] = min(dp[i+j], dp[i] + abs(h[i] - h[i+j]))

print(dp[-1])
