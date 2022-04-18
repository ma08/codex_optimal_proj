#!/usr/bin/env python

import sys

def main():
    n = int(sys.stdin.readline())
    trips = {}
    for _ in range(n):
        country, year = sys.stdin.readline().split()[:2]
        if country in trips:
            trips[country].append(year)
        else:
            trips[country] = [year]
    q = int(sys.stdin.readline())
    for _ in range(q):
        country, k = sys.stdin.readline().split()[:2]
        print(trips[country][int(k) - 1])

if __name__ == "__main__":
    main()
