

import math
import sys

def main():
    a, b, h, m = map(int, sys.stdin.readline().rstrip().split())
    short_hand = (math.pi * (h * 60 + m) / 360) % (math.pi * 2)
    long_hand = (math.pi * 6 * m / 360) % (math.pi * 2)
    print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(short_hand - long_hand)))

if __name__ == "__main__":
    main()
