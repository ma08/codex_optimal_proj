

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(1, n):
        if a[i] > a[i - 1]:
            dp[i][0] = dp[i - 1][0] + 1
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0])
        else:
            dp[i][0] = 1
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0])
    print(max(dp[n - 1]))
    ans = ""
    i = n - 1
    while i >= 0:
        if dp[i][0] > dp[i][1]:
            ans += "L"
            i -= 1
        else:
            ans += "R"
            i -= dp[i][1]
    print(ans[::-1])

if __name__ == "__main__":
    main()
