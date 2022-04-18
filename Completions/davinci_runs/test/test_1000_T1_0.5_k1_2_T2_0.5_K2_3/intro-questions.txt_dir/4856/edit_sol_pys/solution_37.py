import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for x in reversed(arr):
    print(x, end=" ")
