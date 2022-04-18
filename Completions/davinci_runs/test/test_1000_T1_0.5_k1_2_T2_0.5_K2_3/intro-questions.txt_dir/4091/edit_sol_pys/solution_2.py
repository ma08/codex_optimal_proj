

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [0]*(n+1) #dp[i]: max value from a[0] to a[i-1]
    for i in range(1,n+1):
        dp[i] = max(dp[i-1],a[i-1])
    # sum of max value in every k-length subarray in a
    ans = 0
    for i in range(k,n+1):
        ans += dp[i-k]
    print(ans)
    i = 0
    while i < n:
        # if j exceed the length of array a
        j = i+k
        if j > n:
            j = n
        while j > i and dp[i] == dp[j]:
            j -= 1
        print(j-i,end=" ")
        i = j
    print()

main()
