

import sys

def main():
    n = int(sys.stdin.readline())
    print(solve(n))

def solve(n):
    MOD = 1000000007
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(i + 1):
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]
            if j < i:
                dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= MOD
    return dp[n][0]

if __name__ == '__main__':
    main()
