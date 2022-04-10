

N, M, X = map(int, input().split())

A = []
C = []
for n in range(N):
    a = list(map(int, input().split()))
    A.append(a)
    C.append(a.pop(0))

# print(A, C)

# dp[i][j] は i 番目までの本を読んで、j 番目のアルゴリズムの理解度が j 以上になるまでにかかる最小コスト
# dp[i][j] = min(dp[i-1][j], dp[i-1][j-A[i][j]] + C[i])
INF = float('inf')

dp = [[INF] * (M+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in range(M+1):
        if j - A[i][j-1] >= 0:
            dp[i+1][j] = min(dp[i][j], dp[i][j-A[i][j-1]] + C[i])
        else:
            dp[i+1][j] = min(dp[i][j], dp[i][j-A[i][j-1]] + C[i])

# print(dp)
if dp[N][X] == INF:
    print(-1)
else:
    print(dp[N][X])