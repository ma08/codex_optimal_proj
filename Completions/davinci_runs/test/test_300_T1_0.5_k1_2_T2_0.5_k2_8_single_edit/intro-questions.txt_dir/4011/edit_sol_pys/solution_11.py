#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().strip()))
    f = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(len(num)):
        num[i] = f[num[i]-1]
    print(' '.join(map(str, num)))


if __name__ == '__main__':
    main()
