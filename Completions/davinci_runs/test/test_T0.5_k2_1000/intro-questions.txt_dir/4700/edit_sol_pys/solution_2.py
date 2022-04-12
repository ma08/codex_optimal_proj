
import sys

n, m = [int(i) for i in input().split()]

h = [int(i) for i in input().split()]  # heights

a = [int(i) for i in input().split()]  # widths

# print(n)
# print(m)
# print(h)
# print(a)


def find_max_height(h, a):
    max_height = 0
    for i in range(m):
        max_height = max(max_height, h[a[i]-1])
    return max_height


max_height = find_max_height(h, a)
print(max_height)
