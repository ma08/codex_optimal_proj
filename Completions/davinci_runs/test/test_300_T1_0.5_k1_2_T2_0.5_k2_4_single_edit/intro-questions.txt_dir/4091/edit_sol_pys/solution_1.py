

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [0]*(n)
    for i in range(1,n):
        dp[i] = max(dp[i-1],a[i])
    ans = 0
    for i in range(k,n):
        ans += dp[i-k]
    print(ans)
    i = 0
    while i <= n:
        j = i+k
        if j > n:
            j = n
        while j > i and dp[i] == dp[j]:
            j -= 1
        print(j-i,end=" ")
        i = j
    print()

main()
