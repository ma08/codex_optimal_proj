
n,m,k = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
dp = [[0] * (k+1) for _ in range(m+1)]
for i in range(n):
    for j in range(1,m+1):
        for l in range(k):
            if j+1>m:
                dp[j][l] = dp[j-1][l]
            else:
                dp[j][l] = max(dp[j-1][l],dp[j-1][(l-a[i][j-1]%k+k)%k]+a[i][j-1])
print(dp[m][0])