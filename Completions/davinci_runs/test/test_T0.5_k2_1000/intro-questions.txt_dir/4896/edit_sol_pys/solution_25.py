
from collections import defaultdict
from sys import stdin

def main():
    n, m = [int(x) for x in stdin.readline().split()]
    graph = defaultdict(list)
    for _ in range(m):
        a, b = [int(x) for x in stdin.readline().split()]
        graph[a].append(b)
        graph[b].append(a)

    print(graph)

if __name__ == '__main__':
    main()
