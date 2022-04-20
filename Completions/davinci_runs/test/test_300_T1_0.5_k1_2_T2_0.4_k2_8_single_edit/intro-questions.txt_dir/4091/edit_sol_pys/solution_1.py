

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [0]*(n+1) # dp[i] = max(a[0:i])
    for i in range(1,n+1):
        dp[i] = max(dp[i-1],a[i-1]) # dp[i] = max(dp[i-1],a[i-1])
    ans = 0
    for i in range(k,n+1): # i = [k,n]
        ans += dp[i-k] # ans += dp[i-k]
    print(ans)
    i = 0 # i = [0,n)
    while i < n:
        j = i+k # j = [i+k,n]
        if j > n:
            j = n
        while j > i and dp[i] == dp[j]: # j = [i,j)
            j -= 1
        print(j-i,end=" ")
        i = j
    print()

main()
