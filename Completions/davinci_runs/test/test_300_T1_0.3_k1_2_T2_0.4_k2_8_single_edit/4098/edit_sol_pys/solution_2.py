

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1 if a[i - 1] - a[i - 2] <= 5 else 1
    print(dp[n] - k + 1)

if __name__ == '__main__':
    main()
