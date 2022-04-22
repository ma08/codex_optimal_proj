import sys
from itertools import product

def main():
    n = int(sys.stdin.readline().rstrip())
    points = []
    for i in range(n):
        x, y, h = map(int, sys.stdin.readline().rstrip().split())
        points.append((x, y, h))
    # print(points)
    for x, y in product(range(101), repeat=2):
        for h in range(101):
            if all(h == height - abs(x - center_x) - abs(y - center_y) for x, y, height in points):
                print(x, y, h)
                sys.exit(0)

if __name__ == "__main__":
    main()
