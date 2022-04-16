
# TODO: implement

import sys
import math

def distance(p1, p2):
    return math.sqrt(sum([(p1[i] - p2[i]) ** 2 for i in range(len(p1))]))


def main():
    n, d = [int(x) for x in sys.stdin.readline().split()]

    points = []
    for _ in range(n):
        points.append([int(x) for x in sys.stdin.readline().split()])

    points = sorted(points, key=lambda x: x[0])

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if distance(points[i], points[j]) % 1 == 0:
                if points[i][0] != points[j][0]:
                    count += 1

    print(count)


if __name__ == '__main__':
    main()
