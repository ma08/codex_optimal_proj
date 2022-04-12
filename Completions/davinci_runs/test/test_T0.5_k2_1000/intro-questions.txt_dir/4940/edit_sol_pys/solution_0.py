#!/usr/bin/env python3

import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    times = []
    for i in range(N):
        times.append(list(map(int, sys.stdin.readline().split())))
    times = sorted(times, key=lambda x: x[0]) # sort by first element
    for i in range(1, M):
        for j in range(N):
            times[j][i] += times[j][i-1] # add previous element
        times = sorted(times, key=lambda x: x[i]) # sort by current element
    print(" ".join(map(str, [times[i][M-1] for i in range(N)])))

main()
