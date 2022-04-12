# https://atcoder.jp/contests/abc081/tasks/abc081_b

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    points = []
    for i in range(n):
        x, y, h = map(int, sys.stdin.readline().rstrip().split())
        points.append((x, y, h))
    # print(points)
    center_x = 0
    center_y = 0
    height = 0
    for center_x in range(101):
        for center_y in range(101):
            for height in range(101):
                if all(h == height - abs(x - center_x) - abs(y - center_y) for x, y, h in points):
                    print(center_x, center_y, height)
                    return

if __name__ == "__main__":
    main()
