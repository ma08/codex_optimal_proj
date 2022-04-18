#!/usr/bin/env python3

from collections import defaultdict, Counter

def main():
    n = int(input())  # number of trips
    trips = defaultdict(list)  # dictionary of trips

    for _ in range(n):
        c, y = input().split()
        trips[c].append(int(y))

q = int(input())

for _ in range(q):
    c, k = input().split()
    print(trips[c][int(k) - 1])
