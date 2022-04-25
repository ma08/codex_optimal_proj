#!/usr/bin/env python3

import sys

def solve(n, a):
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if (a[i] > a[j] and dp[i] < dp[j] + 1):
                dp[i] = dp[j] + 1
    return dp

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    dp = solve(n, a)
    print(max(dp))
    for i, d in enumerate(dp):
        if d == max(dp):
            print(i - d + 2, i + 1)

if __name__ == '__main__':
    main()
