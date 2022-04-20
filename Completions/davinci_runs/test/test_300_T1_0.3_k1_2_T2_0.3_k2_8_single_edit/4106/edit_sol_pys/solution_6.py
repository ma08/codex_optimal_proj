

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))[:n]
    dp = [0]*(n+1)
    for i in range(n):
        for j in range(k):
            if i-j >= 0:
                dp[i] = max(dp[i], dp[i-j-1]+a[i])
    print(dp[n-1])

main()
