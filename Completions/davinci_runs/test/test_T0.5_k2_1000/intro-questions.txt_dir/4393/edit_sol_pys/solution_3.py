#!/usr/bin/env python3

import sys

def main():
    n = int(input())

    t = input()

    s = []

    for i in range(n):
        if t[i] != t[i-1]:
            s.append(t[i])

    print(''.join(s))

if __name__ == '__main__':
    main()
