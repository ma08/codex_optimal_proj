

import math
import itertools

n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def distance_2(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def path_distance(path):
    dist = 0
    for i in range(len(path) - 1):
        dist += distance(path[i], path[i + 1])
    return dist

def path_distance_2(path):
    dist = 0
    for i in range(len(path) - 1):
        dist += distance_2(path[i], path[i + 1])
    return dist

def path_distance_3(path):
    dist = 0
    for i in range(len(path) - 1):
        dist += distance_3(path[i], path[i + 1])
    return dist

def distance_3(p1, p2):
    return (p1[0] - p2[0]) * (p1[1] - p2[1])

def path_distance_4(path):
    dist = 0
    for i in range(len(path) - 1):
        dist += distance_4(path[i], path[i + 1])
    return dist

def distance_4(p1, p2):
    return (p1[0] * p2[1] - p1[1] * p2[0])

def path_distance_5(path):
    dist = 0
    for i in range(len(path) - 1):
        dist += distance_5(path[i], path[i + 1])
    return dist

def distance_5(p1, p2):
    return (p1[0] * p2[0] + p1[1] * p2[1])

paths = itertools.permutations(points)
distances = [path_distance(path) for path in paths]

print(sum(distances) / len(distances))