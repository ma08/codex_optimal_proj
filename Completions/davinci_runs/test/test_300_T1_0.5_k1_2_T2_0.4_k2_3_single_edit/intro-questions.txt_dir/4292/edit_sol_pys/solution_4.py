import sys
import math


n = int(sys.stdin.readline())
arr = [int(i) for i in sys.stdin.readline().split()]

max_val = max(arr)
min_val = min(arr)

max_idx = arr.index(max_val)
min_idx = arr.index(min_val)

print(max_idx, min_idx)
print(max_val, min_val)

if max_idx > min_idx:
    print(max_idx + n - min_idx - 2)
else:
    print(max_idx + n - min_idx - 1)
