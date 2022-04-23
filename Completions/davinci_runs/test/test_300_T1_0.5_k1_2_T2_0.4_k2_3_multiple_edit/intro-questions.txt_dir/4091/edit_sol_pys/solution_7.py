

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [0]*(n+1)
    for i in range(1,n+1):
        dp[i] = max(dp[i-1],a[i-1])
    ans = 0
        ans += dp[i]
    for i in range(k,n+1):
        ans += dp[i-k]
    print(ans-dp[k])

main()
