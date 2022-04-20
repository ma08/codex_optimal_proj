

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # dp[i][j] = number of ways to renumber a[:i] so that a[i] = j
    dp = [[0] * 3 for _ in range(n)]
    dp[0][a[0]] = 1
    for i in range(1, n): 
        dp[i][a[i]] = dp[i - 1][a[i]]
        dp[i][a[i] - 1] = dp[i - 1][a[i] + 1]
        dp[i][a[i] + 1] = dp[i - 1][a[i] - 1]

    print(sum(dp[-1]) % MOD)


MOD = 998244353

if __name__ == '__main__':
    main()
