#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().split()
    for i in range(n):
        s[i] = int(s[i])
    s.sort()
    for i in range(n):
        s[i] = str(s[i])
    print(' '.join(s))


if __name__ == "__main__":
    main()
