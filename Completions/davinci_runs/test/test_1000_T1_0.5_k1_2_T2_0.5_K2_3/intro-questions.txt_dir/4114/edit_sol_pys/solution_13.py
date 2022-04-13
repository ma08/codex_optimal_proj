
import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    points = []
    for i in range(n):
        x, y, h = map(int, sys.stdin.readline().rstrip().split())
        points.append((x, y, h))
    center_x = 0
    center_y = 0
    height = 0
    for x1, y1, h1 in points:
        for x2, y2, h2 in points:
            if x1 == x2 and y1 == y2:
                continue
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2
            height = h1 + abs(x1 - center_x) + abs(y1 - center_y)
            # print(x1, y1, h1, x2, y2, h2, center_x, center_y, height)
            if all(h == max(height - abs(x - center_x) - abs(y - center_y), 0) for x, y, h in points):
                break;
        else:
            continue
        break
    print(center_x, center_y, height)

if __name__ == "__main__":
    main()
