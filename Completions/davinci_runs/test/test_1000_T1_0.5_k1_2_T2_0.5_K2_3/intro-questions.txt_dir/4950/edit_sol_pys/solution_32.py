#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.stdin.readline().strip())
    roads = []

    for i in range(n):
        t, d = map(int, sys.stdin.readline().strip().split())
        roads.append((t, d))

    max_speed = 0
    for i in range(1, n):
        max_speed = max(max_speed, (roads[i][1] - roads[i - 1][1]) / (roads[i][0] - roads[i - 1][0]))

    print(int(max_speed) + 1)

if __name__ == '__main__':
    main()
