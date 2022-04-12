#!/usr/bin/python

import sys

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        num = int(sys.stdin.readline().strip())
        print(solve(num))

def solve(num):
    num = str(num)
    length = len(num)
    if length == 1:
        return int(num)
    else:
        return int(num[0])**(length-1) + int(num[1:])

if __name__ == '__main__':
    main()
