

import itertools
import math

def main():
    N = int(input())
    towns = []
    for i in range(N):
        x, y = map(int, input().split())
        towns.append((x, y))

    paths = list(itertools.permutations(towns))
    total_distance = 0
    for path in paths:
        distance = 0
        for i in range(len(path) - 1):
            distance += math.sqrt((path[i][0] - path[i + 1][0])**2 + (path[i][1] - path[i + 1][1])**2)
        total_distance += distance

    print(total_distance / len(paths))

if __name__ == "__main__":
    main()