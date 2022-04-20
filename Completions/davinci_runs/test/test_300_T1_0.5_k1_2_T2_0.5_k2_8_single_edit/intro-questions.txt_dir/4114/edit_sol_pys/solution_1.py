
import sys


def main():
    N = int(sys.stdin.readline().rstrip())
    points = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    center_x = 0
    center_y = 0
    height = 0
    for x, y, h in points:
        if h > 0:
            center_x = x
            center_y = y
            height = h
            break
    for cx in range(101):
        for cy in range(101):
            h = height
            for x, y, h_ in points:
                if h_ == 0:
                    h = max(h, abs(cx - x) + abs(cy - y))
                elif h_ != abs(cx - x) + abs(cy - y) + h:
                    break
            else:
                print(cx, cy, h)
                return


if __name__ == "__main__":
    main()
