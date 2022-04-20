

n, k, x = [int(x) for x in input().split()]
a = [int(x) for x in input().split()] 

def dp(n, k, x, a):
    dp = [[[-1 for _ in range(x+1)] for _ in range(k)] for _ in range(n)]

    for i in range(k):
        dp[0][i][1] = sum(a[:i+1])
    
    for i in range(1, n):
        for j in range(k): 
            if i+j >= n: break
            for l in range(2, x+1): 
                for m in range(i+j+1, n): 
                    if j+m-i+1 >= k: 
                        dp[i][j][l] = max(dp[i][j][l], sum(a[i:i+j+1]) + dp[m][j+m-i+1-k][l-1])
    
    return max([max(x) for x in dp[0][0]])

print(dp(n,k,x,a))
