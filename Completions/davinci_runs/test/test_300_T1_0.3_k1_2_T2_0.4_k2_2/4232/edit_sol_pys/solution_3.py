#!/usr/bin/env python3

import sys

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    print(a.index(1) + 1)

if __name__ == '__main__':
    main()
