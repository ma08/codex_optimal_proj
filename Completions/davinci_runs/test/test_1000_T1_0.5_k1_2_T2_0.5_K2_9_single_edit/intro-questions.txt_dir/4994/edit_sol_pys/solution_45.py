

import sys

def main():
    points = []
    for i in range(3):
        points.append(list(map(int, sys.stdin.readline().split())))
    x = set([p[0] for p in points])
    y = set([p[1] for p in points])
    if len(x) == 3:
        print(x.pop(), y.pop())
    else:
        print(x.pop(), y.pop())

main()
