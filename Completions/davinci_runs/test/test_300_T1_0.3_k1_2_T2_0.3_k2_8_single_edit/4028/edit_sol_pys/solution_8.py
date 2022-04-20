#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    print(solve(n, s))

def solve(n, s):
    MOD = 10 ** 9 + 7
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(i + 1):
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]
            if j < i:
                dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= MOD
    return dp[n][s.count('(') - s.count(')')]

if __name__ == '__main__':
    main()
