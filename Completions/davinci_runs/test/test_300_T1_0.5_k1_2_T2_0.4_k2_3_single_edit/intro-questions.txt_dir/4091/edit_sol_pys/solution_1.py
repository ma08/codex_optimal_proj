

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], a[i - 1])
    print(dp)


main()
