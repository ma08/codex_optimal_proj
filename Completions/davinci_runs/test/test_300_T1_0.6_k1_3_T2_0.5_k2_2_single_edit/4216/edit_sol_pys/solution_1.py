#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())

    min_f = 10**10
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            a, b = i, n // i
            f = max(len(str(a)), len(str(b)))
            if f < min_f:
                min_f = f

    print(min_f)


if __name__ == '__main__':
    main()
