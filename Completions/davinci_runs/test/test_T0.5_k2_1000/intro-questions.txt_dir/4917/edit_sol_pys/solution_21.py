#!/usr/bin/env python3

import sys

def solve(times):
    # if any time is within another time, it is impossible
    # otherwise, possible
    for t in times:
        for o in times:
            if t != o and t[0] >= o[0] and t[1] <= o[1]:
                return "gunilla is right"
    return "gunilla has a point"

def main():
    n = int(sys.stdin.readline().strip())
    times = []
    for _ in range(n):
        times.append(tuple(map(int, sys.stdin.readline().strip().split())))
    print(solve(times))

if __name__ == "__main__":
    main()
