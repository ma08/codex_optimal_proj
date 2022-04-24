import sys
import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def is_inside(x, y, r, x1, y1, x2, y2):
    if distance(x, y, x1, y1) <= r and distance(x, y, x2, y2) <= r:
        return True
    return False

def main():
    n = int(sys.stdin.readline())
    segments = []
    for i in range(n):
        s = [int(x) for x in sys.stdin.readline().split()]
        segments.append(s)
    segments.sort(key=lambda x:x[0])
    i = 0
    while i < n - 1:
        if segments[i][1] < segments[i + 1][0]:
            del segments[i + 1]
            n -= 1
        elif segments[i][1] < segments[i + 1][1]:
            del segments[i + 1]
            n -= 1
        else:
            i += 1
    segs = [0] * n
    for i in range(n):
        segs[i] = segments[i][1] - segments[i][0]
    segs.sort()
    if n > 1:
        print(segs[n - 2])
    else:
        print(0)

main()
