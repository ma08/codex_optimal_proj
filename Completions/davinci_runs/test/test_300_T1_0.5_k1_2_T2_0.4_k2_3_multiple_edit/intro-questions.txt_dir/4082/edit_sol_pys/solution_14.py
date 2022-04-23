
def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [1] * n
    dp_rev = [1] * n
    for i in range(1, n):
        if a[i] > a[i - 1]:
            dp[i] = dp[i - 1] + 1
        if a[n - i] > a[n - i - 1]:
            dp_rev[n - i - 1] = dp_rev[n - i] + 1

    ans = 0
    for i in range(n):
        if i == 0:
            ans = max(ans, dp[i + 1])
        elif i == n - 1:
            ans = max(ans, dp_rev[i - 1])
        else:
            ans = max(ans, dp[i + 1] + dp_rev[i - 1] - 1)
    print(ans)


if __name__ == "__main__":
    main()
