#!/usr/bin/env python3

import sys

def main():
    n = int(input())
    trips = {}
    for _ in range(n):
        country, year = input().split()
        if country in trips:
            trips[country].append(year)
        else:
            trips[country] = [year]
    q = int(input())
    for _ in range(q):
        country, k = input().split()
        print(trips[country][int(k) - 1])

if __name__ == "__main__":
    main()
