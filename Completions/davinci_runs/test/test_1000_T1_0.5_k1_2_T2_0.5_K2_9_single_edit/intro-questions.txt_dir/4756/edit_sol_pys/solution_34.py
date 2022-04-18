
import sys
import math

def find_closest_point(x1, y1, x2, y2, x3, y3):
    px = x2-x1
    py = y2-y1
    something = px*px + py*py
    u =  ((x3 - x1) * px + (y3 - y1) * py) / float(something) #what is this for?
    if u > 1:
        u = 1
    elif u < 0:
        u = 0
    x = x1 + u * px
    y = y1 + u * py
    dx = x - x3
    dy = y - y3
    dist = math.sqrt(dx*dx + dy*dy)
    return dist

def main():
    n = int(sys.stdin.readline())
    points = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x,y))
    points = sorted(points, key=lambda x: x[1])
    # print points
    min_dist = 100000
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                dist = find_closest_point(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1])
                if dist < min_dist:
                    min_dist = dist
    print("%.6f" % min_dist)

if __name__ == '__main__':
    main()
