

import sys

n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

min_diff = sys.maxsize
min_diff_idx = 0
for i, h_i in enumerate(h):
    diff = abs(a - (t - 0.006 * h_i))
    if diff < min_diff:
        min_diff = diff
        min_diff_idx = i

print(min_diff_idx + 1)