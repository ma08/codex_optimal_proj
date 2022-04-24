
# -*- coding: utf-8 -*-


def solve(a, b, c):
    return min(b // a, c)
import sys


def main():
    # input
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    # main
    ans = solve(a, b, c)

    # output
    print(ans)


if __name__ == '__main__':
    main()
