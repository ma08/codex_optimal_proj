
def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [0]*(n+1) # dp[i] = max(a[j]) where i <= j < k+i
    for i in range(1,n+1):
        dp[i] = max(dp[i-1],a[i-1])
    ans = 0 # answer
    for i in range(k,n+1):
        ans += dp[i-k]
    print(ans)
    i = 0 # index
    while i < n:
        j = min(i+k,n)
        while j > i and dp[i] == dp[j]:
            j -= 1
        print(j-i,end=" ")
        i = j
    print()

main()
