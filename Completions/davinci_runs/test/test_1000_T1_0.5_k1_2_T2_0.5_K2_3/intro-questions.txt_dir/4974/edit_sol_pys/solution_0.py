# -*- coding: utf-8 -*-

import sys

def main():
    r, n = map(int, sys.stdin.readline().split())
    booked = [0] * n
    for _ in range(n):
        booked[_] = int(sys.stdin.readline())
    booked.sort()
    for i in range(1, r):
        if i not in booked:
            print(i)
            return
    print("too late")

if __name__ == '__main__':
    main()
