
from collections import defaultdict
import sys

def main():
    n, m, k = [int(x) for x in sys.stdin.readline().split()]
    roads = [[int(x) for x in sys.stdin.readline().split()] for _ in range(m)]
    # print(n, m, k)
    # print(roads)
    
    graph = defaultdict(set)
    for road in roads:
        graph[road[0]].add(road[1])
        graph[road[1]].add(road[0])

    print(graph)

if __name__ == "__main__":
    main()
