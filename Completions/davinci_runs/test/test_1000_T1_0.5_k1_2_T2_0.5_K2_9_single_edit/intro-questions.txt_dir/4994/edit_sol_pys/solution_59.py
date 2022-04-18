

import sys

def main():
    points = []
    for i in range(3):
        points.append(list(map(int, sys.stdin.readline().split())))
    x = set([point[0] for point in points])
    y = set([point[1] for point in points])
    if len(x) == 3:
        print(x.pop(), y.pop())
    else:
        print(x.pop(), y.pop())

main()
