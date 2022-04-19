#!/usr/bin/env python3

import math

def main():
    n, d = map(int, input().split()) # n is the number of points, d is the number of dimensions
    points = []
    for i in range(n):
        points.append(list(map(int, input().split()))) # points is a list of lists
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            distance = 0
            for k in range(d):
                distance += (points[i][k] - points[j][k]) ** 2
            if math.sqrt(distance).is_integer():
                count += 1
    print(count)

if __name__ == '__main__':
    main()
