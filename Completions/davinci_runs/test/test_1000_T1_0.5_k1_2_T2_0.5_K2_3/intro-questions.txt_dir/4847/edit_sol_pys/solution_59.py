
from sys import stdin

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

def point_in_triangle(x1, y1, x2, y2, x3, y3, px, py):
    a1 = area(x1, y1, x2, y2, px, py)
    a2 = area(x1, y1, x3, y3, px, py)
    a3 = area(x2, y2, x3, y3, px, py)
    return abs(a1 + a2 + a3 - area(x1, y1, x2, y2, x3, y3)) < 0.000001

x1, y1, x2, y2, x3, y3 = map(int, stdin.readline().split())

n = int(stdin.readline())

trees = 0
for _ in range(n):
    px, py = map(int, stdin.readline().split())
    if point_in_triangle(x1, y1, x2, y2, x3, y3, px, py):
        trees += 1

print("{:.1f}".format(area(x1, y1, x2, y2, x3, y3)))
print(trees)
