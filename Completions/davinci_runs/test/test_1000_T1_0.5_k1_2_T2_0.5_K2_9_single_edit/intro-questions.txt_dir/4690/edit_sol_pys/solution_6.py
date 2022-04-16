#!/usr/bin/env python3

import sys

def area_of_rect(a,b,c,d):
    return max(a*b, c*d)

def main():
    a,b,c,d = map(int, sys.stdin.readline().split())
    print(area_of_rect(a,b,c,d))

if __name__ == '__main__':
    main()
