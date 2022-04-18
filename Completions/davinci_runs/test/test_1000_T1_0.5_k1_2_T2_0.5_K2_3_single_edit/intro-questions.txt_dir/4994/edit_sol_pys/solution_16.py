

import sys

def main():
    points = []
    for i in range(3):
        points.append(list(map(int, sys.stdin.readline().split())))
    x = set([x[0] for x in points])
    y = set([y[1] for y in points])
    if len(x) == 3:
        print(x.pop(), y.pop(), sep=' ')
    else:
        print(x.pop(), y.pop(), sep=' ')

main()
