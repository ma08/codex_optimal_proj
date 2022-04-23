import sys
import math
import collections

def distance(p1, p2, d):
    return math.sqrt(sum([(p1[i] - p2[i])**2 for i in range(d)]))

def main():
    n, d = [int(x) for x in sys.stdin.readline().split()]
    points = collections.defaultdict(int)
    count = 0
    for _ in range(n):
        p = tuple([int(x) for x in sys.stdin.readline().split()])
        points[p] += 1

    for p1 in points.keys():
        for p2 in points.keys():
            if p1 == p2:
                continue
            if distance(p1, p2, d) % 1 == 0:
                count += points[p1] * points[p2]

    print(count//2)


if __name__ == '__main__':
    main()
