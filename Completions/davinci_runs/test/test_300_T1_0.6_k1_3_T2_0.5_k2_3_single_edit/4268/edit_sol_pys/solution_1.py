
import math
from sys import stdin

stdin.readline()
points = [tuple(map(int, line.strip().split())) for line in stdin.readlines()]

def is_integer(n):
    return n == int(n)

# This is O(n^2) time and O(n^2) space.
def num_pairs_with_integer_distance(points):
    num_pairs = 0
    distances = {}
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            distance = math.sqrt(sum((x1 - x2)**2 for x1, x2 in zip(p1, p2)))
            if is_integer(distance):
                num_pairs += 1
    return num_pairs

print(num_pairs_with_integer_distance(points))
