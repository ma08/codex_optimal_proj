
import sys
import math
import heapq
import bisect
import random
import itertools
import collections
import functools

def solve(n, a, m, segs, dp):
    if n == 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    ans = a[n-1]
    for i in range(m):
        if segs[i][0] <= n:
            ans = max(ans, a[n-1] + solve(n-segs[i][0], a, m, segs, dp))
    dp[n] = ans
    return ans

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    segs = []
    for i in range(m):
        l, r = map(int, input().split())
        segs.append((l, r))
    ans, q, c = solve(n, a, m, segs)
    print(ans)
    print(q)
    print(' '.join(map(str, c)))

if __name__ == '__main__':
    main()
