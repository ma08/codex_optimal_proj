#!/usr/bin/env python3

import sys

def read_ints():
    return [int(i) for i in sys.stdin.readline().strip().split(' ')]

def solve(n, preferences):
    # sort by lower bound
    preferences.sort(key=lambda pref: pref[0])

    # greedy
    rooms = 0
    for pref in preferences:
        if rooms == 0 or pref[0] > rooms:
            rooms = pref[1]

    return rooms

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    preferences = [read_ints() for _ in range(n)]
    print(solve(n, preferences))
