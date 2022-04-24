
import math


def get_largest_subset(n, points):
    
    largest_subset = [points[0]]
    for i in range(1, n):
        for j in range(i):
            if math.log(abs(points[i] - points[j]), 2) % 1 == 0:
                largest_subset.append(points[i])
    return largest_subset


def read_input():
    
    n = int(input())
    points = [int(i) for i in input().split()]
    return n, points


if __name__ == '__main__':
    n, points = read_input()
    largest_subset = get_largest_subset(n, points)
    print(len(largest_subset))
    print(*largest_subset)
