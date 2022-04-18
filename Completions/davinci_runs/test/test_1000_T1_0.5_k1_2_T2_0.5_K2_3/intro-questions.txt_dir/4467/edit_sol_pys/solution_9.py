# coding: utf-8
import sys
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pair:
    def __init__(self, r, b):
        self.r = r
        self.b = b

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def is_inside(self, x, y):
        return (self.x - x)**2 + (self.y - y)**2 <= self.r**2

    def is_intersects(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2 <= (self.r + other.r)**2

    def area(self):
        return math.pi * self.r**2

    def intersect_area(self, other):
        if self.is_intersects(other):
            return self.area() + other.area() - (self.r + other.r)**2
        else:
            return 0

def main():
    n = int(sys.stdin.readline())
    r = []
    b = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        r.append(Point(x, y))
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        b.append(Point(x, y))
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            r_circle = Circle(r[i].x, r[i].y, r[i].x - r[j].x)
            b_circle = Circle(b[i].x, b[i].y, b[i].x - b[j].x)
            if r_circle.is_inside(b[j].x, b[j].y):
                cnt += 1
            if b_circle.is_inside(r[j].x, r[j].y):
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
