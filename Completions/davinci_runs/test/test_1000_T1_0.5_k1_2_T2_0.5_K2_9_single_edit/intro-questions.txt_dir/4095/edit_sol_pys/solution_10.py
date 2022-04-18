

import sys
import math

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    print(solve(n, m, p) % 998244353)

def solve(n, m, p):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(m+1):
            dp[i][j] = dp[i-1][j]
            if j >= p[i-1]:
                dp[i][j] += dp[i-1][j-p[i-1]]
    return dp[n][m]

if __name__ == "__main__":
    main()
