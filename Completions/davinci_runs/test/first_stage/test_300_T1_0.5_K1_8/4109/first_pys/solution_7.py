

# Input
N, M, X = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
C = list(map(int, input().split()))

# Solve
INF = float('inf')
dp = [INF] * (2 ** M)
dp[0] = 0
for s in range(2 ** M):
    for i in range(N):
        n_s = s
        for j in range(M):
            if s >> j & 1 == 0 and A[i][j] > 0:
                n_s += 2 ** j
        dp[n_s] = min(dp[n_s], dp[s] + C[i])

ans = dp[-1]
if ans == INF:
    print(-1)
else:
    print(ans)