

import sys, math

n, m = [int(i) for i in sys.stdin.readline().split()]
a = [int(i) for i in sys.stdin.readline().split()]
a.sort()

def find_min_diff(a, n, m):
    min_diff = math.inf
    for i in range(n-m+1):
        diff = a[i+m-1] - a[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

print(find_min_diff(a, n, m))
