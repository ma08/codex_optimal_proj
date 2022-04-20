

from math import *

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(float, input().split())
        points.append((x, y))

    print(degree(points))

def degree(points):
    l = len(points)
    if l == 1:
        return 0
    elif l == 2:
        x1, y1 = points[0]
        x2, y2 = points[1]
        return rad2deg(atan((y2-y1)/(x2-x1)))
    else:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]

        a = sqrt((x1-x2)**2+(y1-y2)**2)
        b = sqrt((x2-x3)**2+(y2-y3)**2)
        c = sqrt((x1-x3)**2+(y1-y3)**2)

        return rad2deg(acos((a**2+b**2-c**2)/(2*a*b)))

def rad2deg(rad):
    return rad*180/pi

if __name__ == '__main__':
    main()