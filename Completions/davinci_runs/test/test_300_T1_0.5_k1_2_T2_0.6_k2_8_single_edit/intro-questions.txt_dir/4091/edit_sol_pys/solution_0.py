

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [0]*n
    for i in range(n):
        dp[i] = max(dp[i-1],a[i])
    ans = 0
    for i in range(k-1,n):
        ans += dp[i-k+1]
    print(ans)
    for i in range(k-1,n):
        print(dp[i-k+1],end=" ")
    print()

main()
