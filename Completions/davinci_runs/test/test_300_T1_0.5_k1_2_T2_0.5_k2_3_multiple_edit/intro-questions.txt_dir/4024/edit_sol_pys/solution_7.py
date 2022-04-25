
N,K=map(int,input().split())
S=input()
dp=[0]*(N+1)
for i in range(1,N+1):
    for j in range(i):
        if S[j:i] in S[:i]:
            dp[i]=max(dp[i],dp[j]+N-i+j)
if dp[N]<K:
    print(-1)
else:
    print(dp[N])
