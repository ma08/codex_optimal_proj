

import sys

def min_diff(s, b, n, index, curr_s, curr_b, min_d, lookup):
    if index == n:
        return abs(curr_s - curr_b)
    if min_d < abs(curr_s - curr_b):
        return min_d
    if (curr_s, curr_b) in lookup:
        return lookup[(curr_s, curr_b)]
    lookup[(curr_s, curr_b)] = min(min_diff(s, b, n, index + 1, curr_s, curr_b, min_d, lookup),
                                   min_diff(s, b, n, index + 1, curr_s * s[index], curr_b + b[index], min_d, lookup))
    return lookup[(curr_s, curr_b)]

n = int(sys.stdin.readline())
s = []
b = []
for i in range(n):
    s_i, b_i = [int(x) for x in sys.stdin.readline().split()]
    s.append(s_i)
    b.append(b_i)
print(min_diff(s, b, n, 0, 1, 0, 100000000, {}))
