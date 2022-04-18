

import sys

def distance(point1):
    return point1[0]**2 + point1[1]**2

def main():
    num_points = int(sys.stdin.readline())
    points = []
    for _ in range(num_points):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x, y))
    count = 0
    for i in range(num_points):
        for j in range(i+1, num_points):
            if int(distance(points[i] - points[j])**0.5) == distance(points[i] - points[j])**0.5:
                count += 1
    print(count)


if __name__ == '__main__':
    main()
