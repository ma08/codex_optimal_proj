#!/usr/bin/env python3

import sys


def solve(n, a):
    sum_ = [0] * (n + 1)
    for i in range(n):
        sum_[i + 1] = sum_[i] + a[i]
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1]
        for j in range(1, i + 1):
            if sum_[i] - sum_[j] == 0:
                dp[i] = max(dp[i], dp[j]+1)
    print(dp[n])
    i = n
    while i > 0:
        j = i-1
        while j > 0:
            if sum_[i] - sum_[j] == 0 and dp[i] == dp[j]+1:
                print(j, i)
                i = j
                break
            j -= 1
        else:
            print(i, i)
            i -= 1

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    solve(n, a)
