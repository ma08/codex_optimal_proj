

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [0]*(n+1)
    dp[1] = a[0]
    for i in range(2,n+1):
        dp[i] = max(dp[i-1],dp[i-2]+a[i-1])
    ans = 0
    for i in range(k,n+1):
        ans += dp[i-k]
    print(ans)
    i = 0
    while i < n:
        j = i+k
        if j > n:
            j = n
        while j > i and dp[i] == dp[j]:
            j -= 1
        print(j-i,end=" ")
        i = j
    print()

main()
