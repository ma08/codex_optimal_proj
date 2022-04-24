
def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = max(dp[i-1], a[i-1])

    ans = sum(dp[k:])
    print(ans, end=" ")
    for i in range(k, n+1):
        if dp[i-k] == dp[i]:
            print(0, end=" ")
        else:
            print(dp[i-k], end=" ")


main()
