

N,M,X = list(map(int, input().split()))
C = []
A = []
for i in range(N):
    c, a = list(map(int, input().split()))
    C.append(c)
    A.append(a)

#dp[i][j] = i番目までの本を読んで、j番目のアルゴリズムのレベルがX以上になるようにするのに必要な最小のお金
#dp[i][j] = min(dp[i-1][j], dp[i-1][j-a[i][j]]+c[i])
dp = [[float('inf')]*(M+1) for i in range(N+1)]
dp[0][0] = 0
for i in range(1,N+1):
    for j in range(M+1):
        if j == 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-A[i-1][j-1]]+C[i-1])

if dp[N][M] == float('inf'):
    print('-1')
else:
    print(dp[N][M])