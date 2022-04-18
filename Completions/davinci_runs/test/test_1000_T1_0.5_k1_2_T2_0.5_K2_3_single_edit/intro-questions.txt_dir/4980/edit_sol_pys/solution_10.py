#!/usr/bin/env python3

import re

import sys

def main():
    n = int(sys.stdin.readline())
    if n == 0:
        return 1
    else:
        counter = 0
        for i in range(n):
            word = sys.stdin.readline().lower()
            if "pink" in word or "rose" in word:
                counter += 1
        if counter == 0:
            print("I must watch Star Wars with my daughter")
        else:
            print(counter)

if __name__ == '__main__':
    main()
