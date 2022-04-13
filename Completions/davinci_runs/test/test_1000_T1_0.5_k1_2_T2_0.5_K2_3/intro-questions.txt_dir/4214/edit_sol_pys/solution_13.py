
from math import sqrt
from itertools import permutations

def dist(p1,p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)

N = int(input())
points = []
for _ in range(N):
    points.append(tuple(map(int,input().split())))

paths = permutations(points)

total_dist = 0
for path in paths:
    dist_in_path = 0
    for i in range(N-1):
        dist_in_path += dist(path[i],path[i+1])
    total_dist += dist_in_path

print(total_dist/len(paths))
