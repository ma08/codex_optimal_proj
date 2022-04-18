#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline().strip())
    pages = 1
    days = 0
    while True:
        if pages >= n:
            break
        days += 1
        pages += pages
    print(days)

if __name__ == '__main__':
    main()
