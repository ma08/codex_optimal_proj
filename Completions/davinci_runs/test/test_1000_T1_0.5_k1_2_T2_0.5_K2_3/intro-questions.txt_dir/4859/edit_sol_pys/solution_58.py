


"""
This is a program that will count the number of ways
you can have a number of legs with a number of cows,
dogs, and chickens
"""

import sys

def legs(b,d,c,l):
    if l<0:
        return 0
    if b == 0 and d == 0 and c == 0:
        print("{} {} {}".format(b,d,c))
        return 1
    legs(b - 1, d, c, l - b)
    legs(b, d - 1, c, l - d)
    return legs(b, d, c - 1, l - c)


def main():
    data = sys.stdin.readline().split()
    b = int(data[0])
    d = int(data[1])
    c = int(data[2])
    l = int(data[3])
    legs(b, d, c, l)


if __name__ == "__main__":
    main()
