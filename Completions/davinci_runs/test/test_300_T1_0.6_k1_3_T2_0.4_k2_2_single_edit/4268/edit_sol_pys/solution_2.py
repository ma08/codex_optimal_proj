

from sys import stdin

stdin.readline()
points = [tuple(map(int, line.strip().split())) for line in stdin.readlines()]

def sq(n):
    return n*n

# This is O(n^2) time and O(n^2) space.
def num_pairs_with_integer_distance(points):
    num_pairs = 0
    distances = {}
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            key = (p1, p2)
            if key in distances:
                continue
            else:
                distances[key] = sum(sq(x1 - x2) for x1, x2 in zip(p1, p2))
            if distances[key] == int(distances[key]):
                num_pairs += 1
    return num_pairs

print(num_pairs_with_integer_distance(points))
