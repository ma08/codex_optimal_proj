

import math
n = int(input())
a = list(map(int, input().split()))

a.sort()

max_num = a[-1]

for i in range(n-2, -1, -1):
    if a[i] == max_num:
        print(max_num)
        break
    if a[i] * 2 <= max_num:
        print(a[i])
        break
