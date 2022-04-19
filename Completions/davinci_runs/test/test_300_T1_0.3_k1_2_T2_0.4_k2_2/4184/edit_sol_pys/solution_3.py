import sys
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())
A = list(map(int, input().split()))

# DP[i][j] = i番目までの荷物から重さの和がjになるように選んだときの、最大の価値
# DP[i][j] = max(DP[i-1][j], DP[i-1][j-A[i]] + A[i])
# DP[i][j] = DP[i-1][j] if j < A[i]
# DP[i][j] = max(DP[i-1][j], DP[i-1][j-A[i]] + A[i]) if j >= A[i]

DP = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(M+1):
        if j < A[i]:
            DP[i+1][j] = DP[i][j]
        else:
            DP[i+1][j] = max(DP[i][j], DP[i][j-A[i]] + A[i])

print(DP[N][M])
