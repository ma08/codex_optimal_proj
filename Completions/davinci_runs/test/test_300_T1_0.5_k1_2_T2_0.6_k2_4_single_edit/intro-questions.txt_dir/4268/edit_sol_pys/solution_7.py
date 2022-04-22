
import math
import sys

def distance(p1, p2):
    return math.sqrt(sum([(p1[i] - p2[i])**2 for i in range(len(p1))]))


def main():
    n, d = [int(x) for x in sys.stdin.readline().split()]
    points = [tuple([int(x) for x in sys.stdin.readline().split()]) for _ in range(n)]

    count = 0
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points[i+1:]):
            if distance(points[i], points[j]) % 1 == 0:
                count += 1
    print(count)


if __name__ == '__main__':
    main()
