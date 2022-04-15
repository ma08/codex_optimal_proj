

import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pair:
    def __init__(self, r, b):
        self.r = r
        self.b = b

def main():
    n = int(sys.stdin.readline())
    r = []
    b = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        r.append(Point(x, y))
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        b.append(Point(x, y))
    pairs = []
    for i in range(n):
        for j in range(n):
            if r[i].x < b[j].x and r[i].y < b[j].y:
                pairs.append(Pair(r[i], b[j]))
    print(len(pairs))

if __name__ == '__main__':
    main()