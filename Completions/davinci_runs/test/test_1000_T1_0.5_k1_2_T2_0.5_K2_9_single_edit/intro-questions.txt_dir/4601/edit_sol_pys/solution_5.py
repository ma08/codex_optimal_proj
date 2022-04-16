#!/usr/bin/env python3

import sys

def solve(N, K, H):
    H.sort()
    if K >= N:
        return 0
    else:
        return sum(H[K:]) - sum(H[:K])

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().rstrip().split())
    H = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solve(N, K, H))
