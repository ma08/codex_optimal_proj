

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]

dp[0][0] = A[0][0]
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        if i == 0:
            dp[i][j] = dp[i][j - 1] + A[i][j]
        elif j == 0:
            dp[i][j] = dp[i - 1][j] + A[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + A[i][j]

print(dp[N - 1][M - 1])
