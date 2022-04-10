

def main():
    N,M,X=map(int,input().split())
    A=[]
    C=[]
    for i in range(N):
        a=list(map(int,input().split()))
        A.append(a[0:M])
        C.append(a[M])
    #dp[i][j] i番目までの本を読んだとき、j番目のアルゴリズムの理解度をX以上にできるのならば、かかる最低金額を格納
    #dp[i][j]=min(dp[i-1][j],dp[i][j]) 
    #dp[i][j]=dp[i-1][j-A[i][j]]+C[i]
    dp=[[float('inf') for j in range(M)] for i in range(N+1)]
    dp[0][0]=0
    for i in range(1,N+1):
        for j in range(M):
            if dp[i-1][j]<=X:
                dp[i][j]=min(dp[i-1][j],dp[i][j])
                if j-A[i-1][j]>=0:
                    dp[i][j]=min(dp[i-1][j-A[i-1][j]]+C[i-1],dp[i][j])
    if dp[N][M-1]==float('inf'):
        print(-1)
    else:
        print(dp[N][M-1])

if __name__ == '__main__':
    main()
