#!/usr/bin/env python3

import sys

def main():
    n, a = map(int, sys.stdin.readline().split())
    e = list(map(int, sys.stdin.readline().split()))

    e.sort()
    count = 0
    for i in range(n):
        if a < e[i]:
            break
        a -= e[i]
        count += 1

    print(count)

if __name__ == "__main__":
    main()
