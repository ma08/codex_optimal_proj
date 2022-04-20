
import math

n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_num = max(arr)

min_num = max_num

for i in range(n):
    if arr[i] < min_num:
        min_num = arr[i]

if min_num == max_num:
    print(0)
    exit(0)

min_divs = math.inf

for div in range(min_num, max_num+1):
    divs = 0
    for i in range(n):
        if arr[i] % div != 0:
            divs += math.ceil(arr[i] / div) - 1
    if divs < min_divs:
        min_divs = divs

print(min_divs)