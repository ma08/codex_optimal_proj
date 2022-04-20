#!/usr/bin/env python3


import sys


def main(args):
    q = int(args[1])
    for i in range(2, q+2):
        n, a, b = map(int, args[i].split())
        print((n//2) * b + (n%2) * a if b < 2*a else n*a)


main(sys.argv)
