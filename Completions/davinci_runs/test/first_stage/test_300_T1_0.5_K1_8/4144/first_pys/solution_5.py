

import sys

MOD = 10**9 + 7

def main():
    N = int(sys.stdin.readline().rstrip())
    dp = [[0]*10 for i in range(N+1)]
    for i in range(1, 10):
        dp[1][i] = 1

    for i in range(2, N+1):
        for j in range(10):
            for k in range(10):
                dp[i][j] += dp[i-1][k]
                dp[i][j] %= MOD

    ans = 0
    for i in range(1, 10):
        ans += dp[N][i]
        ans %= MOD

    print(ans)

if __name__ == '__main__':
    main()