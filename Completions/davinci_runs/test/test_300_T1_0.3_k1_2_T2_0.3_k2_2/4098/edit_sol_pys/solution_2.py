
def main():
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if a[i] - a[j] <= 5:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp) - k)

if __name__ == '__main__':
    main()
