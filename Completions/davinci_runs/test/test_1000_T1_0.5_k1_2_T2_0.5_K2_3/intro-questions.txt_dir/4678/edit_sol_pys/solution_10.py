

from bisect import bisect_left, bisect_right

n = int(input())
a = sorted(list(map(int, input().split())))

print(bisect_right(a, a[0]))
print(bisect_left(a, a[0]))
