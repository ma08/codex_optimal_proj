

def main():
    n = int(input()) + 1
    a = [0] + [int(x) for x in input().split()]
    dp = [0] * n
    dp[1] = a[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + a[i])
    print(dp[n - 1])

main()
