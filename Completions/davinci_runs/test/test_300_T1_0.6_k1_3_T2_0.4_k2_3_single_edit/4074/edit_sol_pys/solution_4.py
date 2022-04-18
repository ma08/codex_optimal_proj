#!/usr/bin/env python3

import sys


def get_min_packets(shovels, types, cache):
    if shovels < 0 or types == 0:
        return sys.maxsize

    if shovels == 0:
        return 0

    if cache[shovels][types] != -1:
        return cache[shovels][types]

    min_packets = sys.maxsize - 1
    for t in range(1, types + 1):
        packets = get_min_packets(shovels - t, types, cache)
        if packets < min_packets:
            min_packets = packets

    cache[shovels][types] = min_packets + 1
    return cache[shovels][types]

def main():
    sys.setrecursionlimit(10**6)
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        N, K = map(int, sys.stdin.readline().strip().split())
        cache = [[-1 for _ in range(K + 1)] for _ in range(N + 1)]
        print(get_min_packets(N, K, cache))

if __name__ == "__main__":
    main()
