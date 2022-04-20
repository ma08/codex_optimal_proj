

#from math import sqrt
#from itertools import permutations
from scipy.spatial.distance import euclidean

def dist(p1,p2):
    return euclidean(p1,p2)

#N = int(input())
N = 3
points = []
for _ in range(N):
    points.append(tuple(map(int,input().split()))) #change to read from csv

#paths = permutations(points)

total_dist = 0
for path in paths:
    dist_in_path = 0
    for i in range(N-1):
        dist_in_path += dist(path[i],path[i+1])
    total_dist += dist_in_path

print(total_dist/N)
