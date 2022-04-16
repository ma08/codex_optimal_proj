

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    points = []
    for i in range(n):
        x, y, h = map(int, sys.stdin.readline().rstrip().split())
        points.append((x, y, h))
    # print(points)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, h1 = points[i]
            x2, y2, h2 = points[j]
            if x1 == x2:
                cx = x1
                cy = (y1 + y2) // 2
                h = h1 + abs(y1 - cy)
            elif y1 == y2:
                cx = (x1 + x2) // 2
                cy = y1
                h = h1 + abs(x1 - cx)
            else:
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2
                h = h1 + abs(x1 - cx) + abs(y1 - cy)
            # print(center_x, center_y, height)
            if all(h == h - abs(x - cx) - abs(y - cy) for x, y, h in points):
                print(cx, cy, h)
                break

if __name__ == "__main__":
    main()
