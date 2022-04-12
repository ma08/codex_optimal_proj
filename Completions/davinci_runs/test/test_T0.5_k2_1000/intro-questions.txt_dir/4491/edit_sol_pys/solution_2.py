# -*- coding: utf-8 -*-

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    A = [int(x) for x in sys.stdin.readline().rstrip().split()]
    dp = [0] * N
    dp[0] = A[0]
    for i in range(1, N - 1):
        dp[i] = max(dp[i - 1], dp[i - 2]) + A[i]
    dp[N - 1] = dp[N - 2] + A[N - 1]
    print(dp[N - 1])

if __name__ == "__main__":
    main()
