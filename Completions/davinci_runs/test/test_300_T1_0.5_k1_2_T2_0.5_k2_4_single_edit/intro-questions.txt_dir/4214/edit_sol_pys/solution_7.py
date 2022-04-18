
from math import sqrt
from itertools import permutations

def dist(p1,p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

N = int(input())
points = [tuple(map(int,input().split())) for _ in range(N)]
paths = permutations(points)

total_dist = 0
for path in paths:
    for i in range(N):
        dist_in_path += dist(path[i],path[(i+1)%N])
    total_dist += dist_in_path/N

print(total_dist/(N*N))
