

def main():
    N, M, X=map(int, input().split())
    A=[]
    C=[]
    for _ in range(N):
        A.append(list(map(int, input().split())))
    for _ in range(N):
        C.append(int(input()))
    inf=float("inf")
    dp=[[[inf for _ in range(X+1)] for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0]=0
    for i in range(N):
        for j in range(M):
            for k in range(X):
                if dp[i][j][k]==inf:
                    continue
                dp[i+1][j][k]=min(dp[i+1][j][k], dp[i][j][k])
                dp[i+1][j+1][k+A[i][j]]=min(dp[i+1][j+1][k+A[i][j]], dp[i][j][k]+C[i])
    ans=inf
    for i in range(M):
        ans=min(ans, dp[N][i][X-1])
    if ans==inf:
        print(-1)
    else:
        print(ans)

if __name__=="__main__":
    main()