

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [0]*(n+1)
    for i in range(n):
        dp[i+1] = max(dp[i],a[i])
    ans = 0
    for i in range(k,n+1): # k,2k,3k,...,n
        ans += dp[i-k]
    print(ans)
    j = 0
    for i in range(n):
        if dp[i+1] != dp[i]:
            print(i-j+1,end=" ")
            j = i+1
    print()

main()
