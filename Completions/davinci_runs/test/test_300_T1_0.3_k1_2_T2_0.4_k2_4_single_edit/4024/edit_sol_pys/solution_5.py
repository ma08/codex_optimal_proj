#!/usr/bin/env python3

import sys

def main():
    n, k = map(int, input().split())
    s = input().strip()
    if k > n:
        print(-1, file=sys.stdout)
        return
    elif k == n:
        print(0, file=sys.stdout)
        return
    else:
        print(n*(k-1), file=sys.stdout)

if __name__ == "__main__":
    main()
