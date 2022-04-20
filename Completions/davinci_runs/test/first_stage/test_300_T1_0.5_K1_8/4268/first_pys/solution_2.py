

import math
import sys

def main():
    lines = sys.stdin.readlines()
    N, D = map(int, lines[0].split())
    points = [list(map(int, line.split())) for line in lines[1:]]
    print(count_pairs_with_integer_distance(points))

def count_pairs_with_integer_distance(points):
    counter = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if is_integer(get_distance(points[i], points[j])):
                counter += 1
    return counter

def get_distance(point1, point2):
    sum = 0
    for dim in range(len(point1)):
        sum += (point1[dim] - point2[dim]) ** 2
    return math.sqrt(sum)

def is_integer(num):
    return num.is_integer()

if __name__ == '__main__':
    main()