import sys


def solve(n, m, edges, color):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    for i in range(n):
        for j in range(len(graph[i])):
            if color[i] == color[graph[i][j]]:
                print('NO')
                return
    print('YES')


    for u, v in edges:
        if color[u - 1] == color[v - 1]:
            print('NO')
            return
    print('YES')
    for u, v in edges:
        if color[u - 1] < color[v - 1]:
            print(0, end='')
        else:
            print(1, end='')


def main():
    reader = (int(x) for x in sys.stdin.readline().split())
    n, m = next(reader), next(reader)
    edges = [[next(reader), next(reader)] for _ in range(m)]
    solve(n, m, edges)


if __name__ == '__main__':
    main()
