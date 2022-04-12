# compute the area of the triangle
import sys


def area(a, b, c):
    return abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2


# check if the point P is inside the triangle

def contains(a, b, c, p):
    return area(a, b, c) == area(a, b, p) + area(a, p, c) + area(p, b, c)


a = tuple(map(int, sys.stdin.readline().split()))
b = tuple(map(int, sys.stdin.readline().split()))
c = tuple(map(int, sys.stdin.readline().split()))

N = int(sys.stdin.readline())

count = 0
for i in range(N):
    p = tuple(map(int, sys.stdin.readline().split()))
    if contains(a, b, c, p):
        count += 1

print("%.1f" % area(a, b, c))
print(count)
