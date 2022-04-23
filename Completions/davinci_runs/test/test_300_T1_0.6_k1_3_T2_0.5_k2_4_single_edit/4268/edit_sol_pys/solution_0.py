

from math import sqrt

points = [(2, 2), (3, 3), (3, 4), (4, 5)]

def distance(p1, p2):
    return sqrt(sum((x1 - x2)**2 for x1, x2 in zip(p1, p2)))

# This is O(n^2) time and O(n) space.
def num_pairs_with_integer_distance(points):
    num_pairs = 0
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            key = tuple(sorted([p1, p2]))
            if distance(p1, p2) == int(distance(p1, p2)):
                num_pairs += 1
    return num_pairs

print(num_pairs_with_integer_distance(points))
