#!/usr/bin/env python3

import sys

def main():
    num = int(sys.stdin.readline())
    v = list(map(int, sys.stdin.readline().split()))

    for i in range(num-1):
        v.sort()
        x = v.pop(0)
        y = v.pop(0)
        v.append((x+y)/2)

    print(v[0])

if __name__ == "__main__":
    main()
