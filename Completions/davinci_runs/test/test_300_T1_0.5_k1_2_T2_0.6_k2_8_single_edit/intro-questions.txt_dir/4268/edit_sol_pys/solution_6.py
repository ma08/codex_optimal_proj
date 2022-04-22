
# TODO: implement

import sys
import math

def distance(p1, p2):
    return math.sqrt(sum([(p1[i] - p2[i])**2 for i in range(len(p1))]))

def main():
    n, d = [int(x) for x in sys.stdin.readline().split()]
    points = []
    for _ in range(n):
        points.append(tuple(int(x) for x in sys.stdin.readline().split()))

    count = 0
    for i, p1 in enumerate(points):
        for p2 in points[i+1:]:
            count += 1 if distance(p1, p2) % 1 == 0 else 0

    print(count)


if __name__ == '__main__':
    main()
