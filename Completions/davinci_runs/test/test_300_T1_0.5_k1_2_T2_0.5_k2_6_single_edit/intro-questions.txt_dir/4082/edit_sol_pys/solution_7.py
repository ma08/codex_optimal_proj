

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [1] * n
    dp2 = [1] * n
    for i in range(1, n):
        if a[i] > a[i - 1]:
            dp[i] = dp[i - 1] + 1
        if a[n - i - 1] > a[n - i]:
            dp2[n - i - 1] = dp2[n - i] + 1

    print(max(dp + dp2))


if __name__ == "__main__":
    main()
