

MOD = 10 ** 9 + 7

N, M = map(int, input().split())
C = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

X = int(input())

dp = [[float('inf')] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(M + 1):
        if j == 0:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + C[i])
        else:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j], dp[i][j - 1] + C[i])
        for k in range(M):
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + C[i] * (X - sum(A[i][k:])))

if dp[N][M] == float('inf'):
    print(-1)
else:
    print(dp[N][M] % MOD)