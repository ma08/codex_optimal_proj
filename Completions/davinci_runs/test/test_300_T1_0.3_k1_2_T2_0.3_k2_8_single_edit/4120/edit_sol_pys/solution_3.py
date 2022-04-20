
from collections import defaultdict
import sys

def main():
    n, m, k = [int(x) for x in sys.stdin.readline().split()]
    roads = [[int(x) for x in sys.stdin.readline().split()] for _ in range(m)]
    roads = sorted(roads, key=lambda x: x[2])
    graph = defaultdict(list)
    for road in roads:
        graph[road[0]].append((road[1], road[2]))
        graph[road[1]].append((road[0], road[2]))
    print(graph)


if __name__ == "__main__":
    main()
