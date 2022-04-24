import math
n = int(input())
a = [int(input()) for i in range(n)]
a.sort()
max_diff = 0
for i in range(n - 1):
    if abs(a[i] - a[i + 1]) > max_diff:
        max_diff = abs(a[i] - a[i + 1])


print(math.ceil(max_diff / 2))
