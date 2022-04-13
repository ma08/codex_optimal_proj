

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0 for _ in range(n)]
    dp[0] = 1
    for i in range(1, n):
        if a[i] > a[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1
    ans = max(dp)
    for i in range(1, n):
        if a[i - 1] < a[i + 1]:
            ans = max(ans, dp[i - 1] + dp[i + 1])

    print(ans)

if __name__ == '__main__':
    main()
