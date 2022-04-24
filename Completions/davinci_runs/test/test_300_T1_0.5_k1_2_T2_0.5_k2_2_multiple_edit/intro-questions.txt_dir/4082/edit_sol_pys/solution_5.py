def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    ans = 0
    for i in range(n):
        ans = max(ans, dp[i])
    print(ans)

if __name__ == '__main__':
    main()
