


def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [1] * n
    for i in range(1, n):
        if a[i] > a[i - 1]:
            dp[i] = dp[i - 1] + 1

    ans = 0
    for i in range(n):
        ans = max(ans, dp[i])
    print(ans)


if __name__ == "__main__":
    main()
