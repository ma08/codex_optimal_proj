
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a + [0]
    dp = [[0, 0] for _ in range(n + 1)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(1, n + 1):
        if a[i + 1] > a[i]:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0]) + 1
        else:
            dp[i][0] = 1
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0])
    print(max(dp[-1]))
    ans = ""
    i = n
    while i > 0:
        if dp[i][0] > dp[i][1]:
            ans += "L"
            i -= 1
        else:
            ans += "R"
            i -= dp[i][1]
    print(ans[::-1])

if __name__ == "__main__":
    main()
