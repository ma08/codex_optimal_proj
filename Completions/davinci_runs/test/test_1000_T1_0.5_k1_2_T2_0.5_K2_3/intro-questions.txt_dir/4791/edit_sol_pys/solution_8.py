
import sys
from math import sqrt

def area(a, b, c, d):
    s = (a + b + c + d) / 2.0
    return sqrt((s - a) * (s - b) * (s - c) * (s - d))


def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    print(area(a, b, c, d))


if __name__ == "__main__":
    main()
