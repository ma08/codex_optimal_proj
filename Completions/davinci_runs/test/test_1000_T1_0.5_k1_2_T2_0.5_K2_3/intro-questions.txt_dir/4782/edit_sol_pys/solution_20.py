#!/usr/bin/env python3

import sys


def main():
    n, m = [int(x) for x in input().split()]
    print((n - 1) * (m - 1))  # print(n*m - n - m + 1)


if __name__ == "__main__":
    main()
