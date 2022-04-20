

N,M,X = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(N)]

C = [int(input()) for _ in range(N)]

INF = 10**9

dp = [INF for _ in range(2**N)]

dp[0] = 0

for s in range(2**N):
    for i in range(N):
        if s>>i&1:
            continue
        flag = True
        for j in range(M):
            if dp[s|1<<i] > dp[s]+C[i] and dp[s]+C[i] < INF:
                dp[s|1<<i] = dp[s]+C[i]
            if dp[s|1<<i] < INF and dp[s|1<<i]+A[i][j] < X:
                flag = False
        if flag:
            print(dp[s|1<<i])
            exit()

print(-1)