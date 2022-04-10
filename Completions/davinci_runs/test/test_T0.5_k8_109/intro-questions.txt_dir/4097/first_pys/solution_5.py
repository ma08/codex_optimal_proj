

from math import ceil
from sys import stdin


def main():
    n = int(stdin.readline())
    b = list(map(int, stdin.readline().split()))
    min_b = min(b)
    max_b = max(b)
    if max_b - min_b > n - 1:
        print(-1)
    else:
        print(n - (max_b - min_b) - 1)


if __name__ == '__main__':
    main()