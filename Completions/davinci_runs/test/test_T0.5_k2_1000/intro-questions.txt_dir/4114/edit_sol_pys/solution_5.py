# https://atcoder.jp/contests/abc081/tasks/abc081_b

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    points = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    center_x = 0
    center_y = 0
    height = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, h1 = points[i][0], points[i][1], points[i][2]
            x2, y2, h2 = points[j][0], points[j][1], points[j][2]
            if x1 == x2:
                center_x = x1
                center_y = (y1 + y2) // 2
                height = h1 + abs(y1 - center_y)
            elif y1 == y2:
                center_x = (x1 + x2) // 2
                center_y = y1
                height = h1 + abs(x1 - center_x)
            else:
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                height = h1 + abs(x1 - center_x) + abs(y1 - center_y)
            # print(center_x, center_y, height)
            if all(h == height - abs(x - center_x) - abs(y - center_y) for x, y, h in points if h > 0):
                print(center_x, center_y, height)
                break

if __name__ == "__main__":
    main()
