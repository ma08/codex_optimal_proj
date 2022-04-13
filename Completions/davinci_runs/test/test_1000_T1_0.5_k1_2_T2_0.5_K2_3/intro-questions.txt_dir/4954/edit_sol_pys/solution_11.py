from collections import defaultdict


def main():
    # get input
    n = int(input())
    graph = defaultdict(set)
    for i in range(n - 1):
        x, y = map(int, input().split())
        graph[x].add(y)
        graph[y].add(x)

    print(graph)

if __name__ == "__main__":
    main()
