

from math import sqrt
from itertools import permutations, combinations

def dist(p1,p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)

N = int(input())
points = [tuple(map(int,input().split())) for _ in range(N)]

paths = combinations(points,2)

total_dist = 0
for path in paths:
    dist_in_path = 0
    dist_in_path += dist(path[0],path[1])
    total_dist += dist_in_path

print(total_dist/N**2)
