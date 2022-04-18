
from sys import stdin
from math import fabs

def area(x1, y1, x2, y2, x3, y3):
    return fabs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

def main():
    x1, y1 = [int(x) for x in stdin.readline().split()]
    x2, y2 = [int(x) for x in stdin.readline().split()]
    x3, y3 = [int(x) for x in stdin.readline().split()]
    n = int(stdin.readline())
    count = 0
    for i in range(n):
        x, y = [int(x) for x in stdin.readline().split()]
        a1 = area(x1, y1, x2, y2, x, y)
        a2 = area(x1, y1, x3, y3, x, y)
        a3 = area(x2, y2, x3, y3, x, y)
        a = area(x1, y1, x2, y2, x3, y3)
        if a1 + a2 + a3 == a:
            count += 1
    print("%.1f" % a)
    print(count)

main()
