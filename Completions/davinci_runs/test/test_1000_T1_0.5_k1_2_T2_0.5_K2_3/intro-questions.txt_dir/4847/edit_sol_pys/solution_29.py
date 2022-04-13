
from sys import stdin

def area(a, b, c):
    return abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2)

def point_in_triangle(a, b, c, p):
    A1 = area(a, b, p)
    A2 = area(a, c, p)
    A3 = area(b, c, p)
    return abs(A1 + A2 + A3 - area(a, b, c)) < 0.000001

a = tuple(map(int, stdin.readline().split()))
b = tuple(map(int, stdin.readline().split()))
c = tuple(map(int, stdin.readline().split()))
n = int(stdin.readline())
trees = 0
for _ in range(n):
    p = tuple(map(int, stdin.readline().split()))
    if point_in_triangle(a, b, c, p):
        trees += 1

print("{:.1f}".format(area(a, b, c)))
print(trees)
