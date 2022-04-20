
import sys
import math
import heapq
import bisect
import random
import itertools
import collections
import functools

def solve(n, a, m, segs):
    segs.sort(key=lambda x: x[1] - x[0])
    segs.reverse()
    # print(segs)
    # print(a)
    ans = 0
    used = [False] * m
    for i in range(m):
        seg = segs[i]
        if not used[i]:
            for j in range(seg[0] - 1, seg[1]):
                a[j] -= 1
            ans += 1
            used[i] = True
            for j in range(i + 1, m):
                seg2 = segs[j]
                if not used[j] and seg2[0] <= seg[0] and seg2[1] >= seg[1]:
                    used[j] = True
    # print(a)
    return max(a) - min(a), ans, [i + 1 for i in range(m) if used[i]]


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
