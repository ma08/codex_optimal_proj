
import sys
from math import sqrt

def area(a, b, c):
    s = (a + b + c) / 2.0
    return sqrt((s - a) * (s - b) * (s - c))


def main():
    a, b, c = map(int, sys.stdin.readline().split())
    print(area(a, b, c))


if __name__ == "__main__":
    main()
