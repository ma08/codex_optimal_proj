#!/usr/bin/env python3

import sys

froshes = int(sys.stdin.readline().strip())
combos = []
for i in range(froshes):
    combo = sorted(list(map(int, sys.stdin.readline().strip().split())))
    combos.append(combo)

combos = sorted(combos)

max_popularity = 1
popularity = 1
for i in range(1, froshes):
    if combos[i] == combos[i-1]:
        popularity += 1
    else:
        popularity = 1
    if popularity > max_popularity:
        max_popularity = popularity

print(max_popularity)
