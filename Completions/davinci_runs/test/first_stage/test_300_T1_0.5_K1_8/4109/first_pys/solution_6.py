

N,M,X=map(int,input().split())
C=[]
A=[]
for i in range(N):
    c,*a=map(int,input().split())
    C.append(c)
    A.append(a)

INF=10**18
dp=[[INF for _ in range(M+1)] for _ in range(N+1)]
dp[0][0]=0

for i in range(N):
    for j in range(M+1):
        if j==0:
            dp[i+1][j]=min(dp[i+1][j],dp[i][j]+C[i])
        else:
            if dp[i][j-1]<=X:
                dp[i+1][j]=min(dp[i+1][j],dp[i][j-1]+C[i])
            else:
                dp[i+1][j]=min(dp[i+1][j],dp[i][j]+C[i])

ans=INF
for i in range(M+1):
    if dp[N][i]<=X:
        ans=min(ans,dp[N][i])

if ans==INF:
    print(-1)
else:
    print(ans)