

#!/usr/bin/env python3

import sys

def read_ints():
    return tuple(map(int, sys.stdin.readline().strip().split()))

def read_array():
    return list(map(int, sys.stdin.readline().strip().split()))

#
#
#

def read_segments():
    n, m = read_ints()
    a = read_array()
    segments = [(l-1, r-1) for l, r in [read_ints() for i in range(m)]]
    return a, segments

#
#
#

def max_diff(a, segments):
    n = len(a)
    
    a_min = min(a)
    a_max = max(a)
    
    if a_min == a_max:
        return 0, ()
    
    s_min = [0] * n
    s_max = [0] * n

    for l, r in segments:
        s_min[l] += 1
        s_max[r] += 1

    d_min = 0
    d_max = 0
    for i in range(n):
        d_min += s_min[i]
        d_max += s_max[i]
        s_min[i] = d_min
        s_max[i] = d_max

    d_min = 0
    d_max = 0
    j = 0
    
    for i in range(n):
        if a[i] == a_min:
            d_min = s_min[i]
        if a[i] == a_max:
            d_max = s_max[i]
            j = i
            break

    return d_max - d_min, s_max[:j]

a, segments = read_segments()

d, s = max_diff(a, segments)

print(d)
print(len(s))
print(' '.join(map(str, s)))