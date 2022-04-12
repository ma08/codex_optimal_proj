#!/usr/bin/env python3
import sys

def main():
    n = int(sys.stdin.readline())
    days = set()
    for i in range(n):
        s, t = map(int, sys.stdin.readline().split())
        for j in range(s, t+1):
            days.add(j)
    print(len(days))

if __name__ == '__main__':
    main()
