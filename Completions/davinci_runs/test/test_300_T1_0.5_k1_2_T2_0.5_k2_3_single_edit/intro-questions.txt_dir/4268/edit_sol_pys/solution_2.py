
# TODO: implement

import sys
import math

def distance(p1, p2):
    return math.sqrt(sum([(p1[i] - p2[i])**2 for i in range(len(p1))])) # pylint: disable=unsubscriptable-object

def main():
    n, d = [int(x) for x in sys.stdin.readline().split()] # pylint: disable=unused-variable
    points = []
    for _ in range(n): # pylint: disable=unused-variable
        points.append(tuple([int(x) for x in sys.stdin.readline().split()]))

    count = 0
    for i in range(n): # pylint: disable=unused-variable
        for j in range(i+1, n): # pylint: disable=unused-variable
            if distance(points[i], points[j]) % 1 == 0:
                count += 1

    print(count)


if __name__ == '__main__':
    main()
