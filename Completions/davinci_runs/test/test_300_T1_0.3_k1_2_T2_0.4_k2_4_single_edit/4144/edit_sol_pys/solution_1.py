import os

import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    dp[1][1] = 1
    for i in range(2, N+1):
        for j in range(1, M+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 1000000007
    print(dp[N][M] % 1000000007)

if __name__ == '__main__':
    main()
