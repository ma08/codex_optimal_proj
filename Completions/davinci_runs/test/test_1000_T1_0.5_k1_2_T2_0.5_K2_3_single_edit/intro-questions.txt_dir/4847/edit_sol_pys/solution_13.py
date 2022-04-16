
from sys import stdin
from math import fabs

def area(x1, y1, x2, y2, x3, y3):
    return fabs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

def main():
    x1, y1 = [int(x) for x in stdin.readline().split()]  # Read triangle points
    x2, y2 = [int(x) for x in stdin.readline().split()]  # Read triangle points
    x3, y3 = [int(x) for x in stdin.readline().split()]  # Read triangle points
    n = int(stdin.readline())
    count = 0
    for i in range(n):
        x, y = [int(x) for x in stdin.readline().split()]  # Read point
        a1 = area(x1, y1, x2, y2, x, y)  # Calculate area for first triangle
        a2 = area(x1, y1, x3, y3, x, y)  # Calculate area for second triangle
        a3 = area(x2, y2, x3, y3, x, y)  # Calculate area for third triangle
        a = area(x1, y1, x2, y2, x3, y3)  # Calculate area for main triangle
        if a1 + a2 + a3 == a:
            count += 1
    print("%.1f" % a)
    print(count)

main()
