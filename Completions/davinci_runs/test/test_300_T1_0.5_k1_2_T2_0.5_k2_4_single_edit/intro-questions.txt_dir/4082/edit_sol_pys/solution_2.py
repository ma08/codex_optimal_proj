

def main():
    n = int(input())
    a.insert(0, -1)
    a.append(10**9+1)
    a = list(map(int, input().split()))
    dp = [0 for _ in range(n)]
    dp[0] = 1
    for i in range(1, n+1):
        if a[i] > a[i-1] and a[i] < a[i+1]:
            dp[i] = dp[i-1] + 1 
        else:
            dp[i] = 1
    ans = max(dp)
    for i in range(1, n+1):
        if a[i-1] < a[i] < a[i+1]:
            ans = max(ans, dp[i-1] + dp[i+1] + 1)
    print(ans)

if __name__ == '__main__':
    main()
