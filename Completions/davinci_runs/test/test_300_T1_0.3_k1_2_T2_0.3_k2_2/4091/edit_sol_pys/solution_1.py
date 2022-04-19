#!/usr/bin/env python
# coding=utf-8

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = map(int, sys.stdin.readline().split())
    a.append(0)
    dp = [[0 for j in range(k+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = dp[i-1][j]
            for l in range(i-1, -1, -1):
                if dp[i][j] < dp[l][j-1] + max(a[l:i]):
                    dp[i][j] = dp[l][j-1] + max(a[l:i])
    print dp[n][k]
    i = n
    j = k
    ans = []
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            for l in range(i-1, -1, -1):
                if dp[i][j] == dp[l][j-1] + max(a[l:i]):
                    ans.append(i-l)
                    i = l
                    j -= 1
                    break
    ans.reverse()
    print ' '.join(map(str, ans))

if __name__ == '__main__':
    main()
