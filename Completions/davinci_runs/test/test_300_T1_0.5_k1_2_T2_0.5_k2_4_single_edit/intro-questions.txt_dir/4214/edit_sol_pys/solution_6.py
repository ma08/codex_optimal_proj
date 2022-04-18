

from math import sqrt
from itertools import permutations, combinations
from copy import deepcopy

def dist(p1, p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)

def all_dist(points):
    dists = []
    for p1, p2 in combinations(points, 2):
        dists.append(dist(p1, p2))
    return dists

def solve(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        dist_in_path = 0
        for i in range(N-1):
            dist_in_path += dist(path[i],path[i+1])
        total_dist += dist_in_path
    return total_dist/N

def solve2(points):
    N = len(points)
    total_dist = 0
    for p1, p2 in combinations(points, 2):
        total_dist += dist(p1, p2)
    return total_dist/N

def solve3(points):
    return sum(all_dist(points))/len(points)

def solve4(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        for i in range(N-1):
            total_dist += dist(path[i],path[i+1])
    return total_dist/N

def solve5(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(path[i],path[i+1]) for i in range(N-1))
    return total_dist/N

def solve6(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(path[i],path[i+1]) for i in range(N-1))
    return total_dist/N

def solve7(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(p1, p2) for p1, p2 in zip(path, path[1:]))
    return total_dist/N

def solve8(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(p1, p2) for p1, p2 in zip(path, path[1:]))
    return total_dist/N

def solve9(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(p1, p2) for p1, p2 in zip(path, path[1:]))
    return total_dist/N

def solve10(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(p1, p2) for p1, p2 in zip(path, path[1:]))
    return total_dist/N

def solve11(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(p1, p2) for p1, p2 in zip(path, path[1:]))
    return total_dist/N

def solve12(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(p1, p2) for p1, p2 in zip(path, path[1:]))
    return total_dist/N

def solve13(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(p1, p2) for p1, p2 in zip(path, path[1:]))
    return total_dist/N

def solve14(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(p1, p2) for p1, p2 in zip(path, path[1:]))
    return total_dist/N

def solve15(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(p1, p2) for p1, p2 in zip(path, path[1:]))
    return total_dist/N

def solve16(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(p1, p2) for p1, p2 in zip(path, path[1:]))
    return total_dist/N

def solve17(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(p1, p2) for p1, p2 in zip(path, path[1:]))
    return total_dist/N

def solve18(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(p1, p2) for p1, p2 in zip(path, path[1:]))
    return total_dist/N

def solve19(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(p1, p2) for p1, p2 in zip(path, path[1:]))
    return total_dist/N

def solve20(points):
    N = len(points)
    paths = permutations(points)
    total_dist = 0
    for path in paths:
        total_dist += sum(dist(p1, p2) for p1, p2 in zip(path, path[1:]))
    return total_dist/N
