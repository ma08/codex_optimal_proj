

import sys


t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    xs = list(map(int, sys.stdin.readline().split()))
    ys = list(map(int, sys.stdin.readline().split()))
    points = [(x, y) for x, y in zip(xs, ys)]
    points.sort()
    platforms = []
    count = 0
    for x, y in points:
        while platforms and y > platforms[0][1]:
            platforms.pop(0)
        if not platforms:
            platforms.append((x, y))
            continue
        if y - platforms[0][1] <= k:
            count += 1
            if len(platforms) > 1 and y + k > platforms[1][1]:
                platforms.pop(0)
                continue
        platforms.append((x, y))
    print(count)
