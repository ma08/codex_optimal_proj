
def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = 0
    for i in range(1, n):
        dp[i] = max(dp[i-1] + 1, dp[i])
    print(dp[n-1])

if __name__ == '__main__':
    main()
