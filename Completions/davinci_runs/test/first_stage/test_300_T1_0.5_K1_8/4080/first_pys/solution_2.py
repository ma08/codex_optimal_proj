

import sys
import os
import math
from collections import defaultdict

def solve(n, m, a, l, r):
    # get min and max of a
    a_min = min(a)
    a_max = max(a)
    a_range = a_max - a_min
    # get max of a[l[i]:r[i]+1]
    max_l_r = -float('inf')
    for i in range(m):
        max_l_r = max(max_l_r, max(a[l[i]-1:r[i]]))
    # compare
    if max_l_r <= a_min:
        return (a_range, 0)
    else:
        # get max of a[l[i]:r[i]+1] - a_min
        max_l_r = -float('inf')
        max_l_r_i = -1
        for i in range(m):
            tmp = max(a[l[i]-1:r[i]]) - a_min
            if tmp > max_l_r:
                max_l_r = tmp
                max_l_r_i = i
        return (a_range, 1, max_l_r_i+1)

def main():
    # read data
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    l = []
    r = []
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        l.append(x)
        r.append(y)
    # solve
    ans = solve(n, m, a, l, r)
    # print answer
    print(ans[0])
    print(ans[1])
    for i in range(2, len(ans)):
        print(ans[i], end=' ')
    print()

if __name__ == '__main__':
    main()