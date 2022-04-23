
from sys import stdin

from math import sqrt
from math import floor
stdin.readline()
points = [tuple(map(int, line.strip().split())) for line in stdin.readlines()]

# This is O(n^2) time and O(n) space.
def num_pairs_with_integer_distance():
    num_pairs = 0
    distances = {}
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            key = tuple(sorted([p1, p2]))
            if key in distances:
                continue
            else:
                distances[key] = sqrt(sum((x1 - x2) ** 2 for x1, x2 in zip(p1, p2)))
            if floor(distances[key]) == distances[key]:
                num_pairs += 1
    return num_pairs

print(num_pairs_with_integer_distance())
