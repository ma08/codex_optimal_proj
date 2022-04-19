

import math

n = input()
arr = list(map(int, input().split()))
print(arr)

for i in range(len(arr)):
    if arr[i] == min(arr):
        print(arr[i], i)
