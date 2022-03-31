

n,k,x = map(int,input().split())
a = list(map(int,input().split()))

if k*x > n:
  print(-1)
else:
  dp = [[0]*(n+1) for _ in range(x+1)]
  for i in range(1,x+1):
    for j in range(k*i,n+1):
      dp[i][j] = max(dp[i][j-1], dp[i-1][j-k]+sum(a[j-k:j]))
  print(dp[x][n])