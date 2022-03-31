

import sys
import numpy as np

# The key observation is that the optimal solution can be obtained by choosing segments which have the most extreme endpoints
# Thus, we can compute the min/max values of all endpoints of segments, then find the optimal solution by choosing the right segments
# If we manage to find the optimal solution, then it is unique.

n, m = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))

min_vals = np.zeros(n)
max_vals = np.zeros(n)
min_vals[:] = np.inf
max_vals[:] = -np.inf

for i in range(m):
    l, r = map(int, sys.stdin.readline().strip().split())
    min_vals[l-1] = min(min_vals[l-1], a[l-1])
    max_vals[r-1] = max(max_vals[r-1], a[r-1])

for i in range(1, n):
    min_vals[i] = min(min_vals[i-1], min_vals[i])
    max_vals[n-1-i] = max(max_vals[n-i], max_vals[n-1-i])

d = 0
selected_segments = []
for i in range(m):
    l, r = map(int, sys.stdin.readline().strip().split())
    d_opt = max(max_vals[r-1], a[r-1]) - min(min_vals[l-1], a[l-1])
    if d_opt > d:
        d = d_opt
        selected_segments = [i+1]
    elif d_opt == d:
        selected_segments.append(i+1)

print(d)
print(len(selected_segments))
print(' '.join(map(str, selected_segments)))