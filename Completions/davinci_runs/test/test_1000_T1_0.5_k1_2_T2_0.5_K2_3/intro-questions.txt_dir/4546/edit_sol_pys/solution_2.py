#!/usr/bin/python

import sys

def main():
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == b:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
