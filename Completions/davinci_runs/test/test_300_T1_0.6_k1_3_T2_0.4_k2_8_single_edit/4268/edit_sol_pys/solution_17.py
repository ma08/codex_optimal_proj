
from math import sqrt
from sys import stdin

stdin.readline()
points = [tuple(map(int, line.strip().split())) for line in stdin.readlines()]

# This is O(n^2) time and O(n) space.
def distance(p1, p2):
    return sqrt(sum((x1 - x2)**2 for x1, x2 in zip(p1, p2)))

def num_pairs_with_integer_distance(points, distance):
    pairs = set()
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if distance(points[i], points[j]) == int(distance(points[i], points[j])):
                pairs.add(tuple(sorted((points[i], points[j]))))
    return len(pairs)

print(num_pairs_with_integer_distance(points, distance))
