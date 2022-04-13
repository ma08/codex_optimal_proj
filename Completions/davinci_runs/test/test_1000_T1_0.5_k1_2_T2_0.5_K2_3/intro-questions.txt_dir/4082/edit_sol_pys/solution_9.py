

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [1 for _ in range(n)]
    for i in range(n):
        if a[i] > a[i-1]:
            dp[i] = dp[i-1] + 1
    ans = max(dp)
    for i in range(n):
        if a[i-1] < a[i+1]:
            ans = max(ans, dp[i-1] + dp[i+1])
    print(ans)

if __name__ == '__main__':
    main()
