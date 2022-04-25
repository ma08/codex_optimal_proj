import os
import sys, math

def get_distance(point_1, point_2):
    return math.sqrt(sum([(point_1[i] - point_2[i])**2 for i in range(len(point_1))]))

def main():
    n, d = [int(i) for i in sys.stdin.readline().split()]
    points = []
    for _ in range(n):
        points.append(tuple([int(i) for i in sys.stdin.readline().split()]))

    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if get_distance(points[i], points[j]) % 1 == 0:
                count += 1

    print(count)

if __name__ == '__main__':
    main()
