

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(i - 1, 0, -1):
            if a[i - 1] - a[j - 1] <= 5:
                dp[i] = max(dp[i], dp[j - 1] + 1)
            else:
                break
    print(dp[n] - k)

if __name__ == '__main__':
    main()