

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(len(arr))

for i in range(len(arr)-1):
    print(arr[i+1], end=' ')
