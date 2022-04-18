#!/usr/bin/python3


import sys

def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        print(a * b + 1)

if __name__ == '__main__':
    main()
