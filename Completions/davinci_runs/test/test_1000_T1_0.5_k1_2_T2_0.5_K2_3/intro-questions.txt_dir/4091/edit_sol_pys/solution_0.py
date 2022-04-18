
def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [0]*(n+1)
    for i in range(0,n):
        dp[i+1] = max(dp[i],a[i])
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
