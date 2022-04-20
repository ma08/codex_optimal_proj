

#n, k = map(int, input().split())
#s = input()

n, k = 4, 5
s = 'asdf'

def sol(n, k, s):
    if k > n*(n+1)//2:
        return -1
    
    # dp[i][j] = min cost to get i chars into j strings
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1] + (n - i)
            if i >= j:
                dp[i][j] = min(dp[i][j], dp[i-j][j] + (n - j))
    
    # dp[i][j] = min cost to get i chars into j strings
    # dp[i][j] = min cost to get i chars into j-1 strings + cost of adding jth string
    #           = min cost to get i-j chars into j-1 strings + cost of adding jth string
    #           = min cost to get i-j chars into j strings + cost of adding jth string
    #           = min cost to get i-j chars into j strings + n - j
    
    # dp[n][j] = min cost to get n chars into j strings
    # dp[n][j] = min cost to get n chars into j-1 strings + cost of adding jth string
    #           = min cost to get n-j chars into j-1 strings + cost of adding jth string
    #           = min cost to get n-j chars into j strings + cost of adding jth string
    #           = min cost to get n-j chars into j strings + n - j
    
    return dp[n][k]

print(sol(n, k, s))