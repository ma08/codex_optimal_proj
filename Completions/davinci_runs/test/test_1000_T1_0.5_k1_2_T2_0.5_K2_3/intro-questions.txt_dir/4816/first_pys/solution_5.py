

import sys
import math

def main():
    x, y, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    min_dist = min(math.hypot(x - x1, y - y1), math.hypot(x - x1, y - y2),
                   math.hypot(x - x2, y - y1), math.hypot(x - x2, y - y2))
    print(min_dist)

if __name__ == "__main__":
    main()