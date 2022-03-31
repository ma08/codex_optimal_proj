#!/usr/bin/env python

import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(i) for i in sys.stdin.readline().split()]
    dp = [1] * n
    for i in range(1, n):
        for j in range(i - 1):
            if a[j] < a[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    print(max(dp))

if __name__ == "__main__":
    main()
