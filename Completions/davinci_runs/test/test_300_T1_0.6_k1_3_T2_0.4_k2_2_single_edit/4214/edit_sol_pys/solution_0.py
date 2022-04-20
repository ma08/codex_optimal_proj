

from itertools import permutations
import math

def calc_length(path):
    length = 0
    for i in range(len(path)-1):
        length += math.sqrt((path[i][0]-path[i+1][0])**2 + (path[i][1]-path[i+1][1])**2)
    return length

def main():
    n = int(input())
    towns = []
    for i in range(n):
        x, y = map(int, input().split())
        towns.append((x, y))
    # print(towns)

    routes = list(permutations(towns))
    # print(routes)

    lengths = []
    for route in routes:
        lengths.append(calc_length(route))
    # print(lengths)

    print(sum(lengths)/len(lengths))

if __name__ == "__main__":
    main()
