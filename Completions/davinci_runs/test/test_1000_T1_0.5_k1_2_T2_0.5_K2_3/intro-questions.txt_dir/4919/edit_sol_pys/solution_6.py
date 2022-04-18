#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    trips = []
    for _ in range(n):
        country, year = sys.stdin.readline().split()[:2]
        trips.append((country, year))
    trips.sort()
    q = int(sys.stdin.readline())
    for _ in range(q):
        country, k = sys.stdin.readline().split()
        k = int(k)
        i = 0
        while k > 0:
            if trips[i][0] == country:
                k -= 1
            i += 1
        print(trips[i-1][1])

if __name__ == "__main__":
    main()
