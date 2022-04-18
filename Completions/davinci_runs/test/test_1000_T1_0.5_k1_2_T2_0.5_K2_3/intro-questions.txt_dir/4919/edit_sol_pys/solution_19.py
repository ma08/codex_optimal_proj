#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    trips = dict()
    for _ in range(n):
        country, year = sys.stdin.readline().split()[:2]
        if country in trips:
            trips[country].append(int(year))
        else:
            trips[country] = [int(year)]
    q = int(sys.stdin.readline())
    for _ in range(q):
        country, k = sys.stdin.readline().split()[:2]
        print(trips[country][int(k)-1])

if __name__ == "__main__":
    main()
