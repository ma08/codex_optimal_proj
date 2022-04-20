
N = int(input())
W = list(map(int, input().split()))

# DP[i][j] = i番目までの荷物から重さの和がjになるように選んだときの、重さの差の最小値
# DP[i][j] = min(DP[i-1][j], DP[i-1][j-W[i]] + W[i])

DP = [[float('inf') for _ in range(sum(W)+1)] for _ in range(N+1)]
DP[0][0] = 0

for i in range(N):
    for j in range(sum(W)+1):
        if j < W[i]:
            DP[i+1][j] = DP[i][j]
        else:
            DP[i+1][j] = min(DP[i][j], DP[i][j-W[i]] + W[i])

ans = float('inf')
for i in range(sum(W)//2+1):
    ans = min(ans, abs(DP[N][i] - (sum(W)-DP[N][i])))
print(ans)
