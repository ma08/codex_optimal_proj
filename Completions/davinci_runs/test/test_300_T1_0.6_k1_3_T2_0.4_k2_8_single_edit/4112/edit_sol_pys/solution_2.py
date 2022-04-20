

n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()] 

def dp(n, k, a):
    dp = [[-1 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, k+1):
            if i == j:
                dp[i][j] = sum(a[:i])
            else:
                dp[i][j] = max(dp[i-1][j], sum(a[i-j:i])+dp[i-j][j])
    return dp[n][k]
print(dp(n,k,a))
