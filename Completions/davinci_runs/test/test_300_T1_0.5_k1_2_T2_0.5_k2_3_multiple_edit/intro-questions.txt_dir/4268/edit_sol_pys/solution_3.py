import sys
import math

def distance(p1, p2, d):
    return math.sqrt(sum([(p1[i] - p2[i])**2 for i in range(d)]))

def main():
    n, d = [int(x) for x in sys.stdin.readline().split()]
    points = []
    for _ in range(n):
        points.append(tuple([int(x) for x in sys.stdin.readline().split()]))

    count = 0
    for i in range(n-1):
        for j in range(i+1, n-1):
            if distance(points[i], points[j], d) % 1 == 0:
                count += 1

    print(int(count))


if __name__ == '__main__':
    main()
