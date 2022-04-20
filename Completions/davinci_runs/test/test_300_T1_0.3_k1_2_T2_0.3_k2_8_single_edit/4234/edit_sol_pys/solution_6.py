#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    if n % 2 == 1:
        print(n)
        print(s)
    else:
        good = True
        for i in range(0, n, 2):
            if s[i] == s[i+1]:
                good = False
                break
        if good:
            print(0)
            print(s)
        else:
            print(n-1)
            print(s[:n-1])

if __name__ == "__main__":
    main()
