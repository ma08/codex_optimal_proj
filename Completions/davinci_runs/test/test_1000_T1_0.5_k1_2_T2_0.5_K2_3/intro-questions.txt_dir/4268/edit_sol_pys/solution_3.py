import sys
import math

import random


def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]

    for _ in range(n):
        l, r = [int(x) for x in sys.stdin.readline().split()]
        print(min(a[l:r+1]))


def main2():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]

    for _ in range(n):
        l, r = [int(x) for x in sys.stdin.readline().split()]
        print(min(a[l:r+1]))


if __name__ == '__main__':
    main()
