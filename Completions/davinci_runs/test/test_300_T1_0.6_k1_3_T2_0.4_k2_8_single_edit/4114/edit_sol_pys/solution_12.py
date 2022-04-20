import sys
input = sys.stdin.readline


def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y, h = map(int, input().split())
        points.append((x, y, h))

# C_X, C_Y is on the line that connects points with altitude 10^9
# C_X, C_Y is on the line that connects points with altitude 10^9-1
# C_X, C_Y is on the line that connects points with altitude 10^9-2
# ...
# C_X, C_Y is on the line that connects points with altitude 1
# C_X, C_Y is on the line that connects points with altitude 0

for cx in range(101):
    for cy in range(101):
        h = 0
        for p in points:
            h = max(h, p[2] - abs(p[0] - cx) - abs(p[1] - cy))
        if h > 0:
            print(cx, cy, h)
            exit()
