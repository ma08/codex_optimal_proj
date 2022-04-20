

import math

def calc_path_length(path):
    path_length = 0
    for i in range(len(path) - 1):
        path_length += math.sqrt((path[i][0] - path[i+1][0])**2 + (path[i][1] - path[i+1][1])**2)
    return path_length

def calc_average_path_length(paths):
    total_path_length = 0
    for path in paths:
        total_path_length += calc_path_length(path)
    return total_path_length / len(paths)

def make_paths(towns):
    if len(towns) == 1:
        return [[towns[0]]]
    paths = []
    for i in range(len(towns)):
        new_towns = towns[:i] + towns[i+1:]
        new_paths = make_paths(new_towns)
        for path in new_paths:
            path.insert(0, towns[i])
            paths.append(path)
    return paths

N = int(input())
towns = []
for i in range(N):
    towns.append(list(map(int, input().split())))

paths = make_paths(towns)
print(calc_average_path_length(paths))