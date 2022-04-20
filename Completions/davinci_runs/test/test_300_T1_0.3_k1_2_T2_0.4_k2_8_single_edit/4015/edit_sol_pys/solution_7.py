#!/usr/bin/python

import sys

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    if n == m:
        print(0)
    elif n > m:
        print(-1)
    else:
        count = 0
        while n < m:
            if m % 2 == 0:
                m = m // 2
            elif m % 3 == 0:
                m = m // 3
            else:
                print(-1)
                return
            count += 1
        print(count)

if __name__ == "__main__":
    main()
