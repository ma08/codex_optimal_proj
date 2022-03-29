

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))

def solve(n, a):
    MOD = 10**9 + 7
    # dp[i][j] = number of good subsequences of length i ending with j
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[j - 1] % i == 0:
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1] + 1) % MOD
            else:
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % MOD
    return dp[n][n]

if __name__ == '__main__':
    main()