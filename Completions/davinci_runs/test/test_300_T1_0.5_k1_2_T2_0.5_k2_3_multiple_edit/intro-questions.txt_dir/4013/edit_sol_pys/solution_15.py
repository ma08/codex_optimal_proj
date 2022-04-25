import math
n = int(input())
arr = [int(x) for x in input().split()]

curr_min = min(arr)
curr_max = max(arr)
a = min(curr_max - curr_min, min(arr.count(curr_min), arr.count(curr_max)))
b = curr_max - curr_min - 2*a

print(b)
