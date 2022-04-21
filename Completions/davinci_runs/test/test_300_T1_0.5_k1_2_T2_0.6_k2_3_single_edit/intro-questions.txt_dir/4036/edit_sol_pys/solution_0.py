from collections import defaultdict

def main():
    n, k = map(int, input().split()) # n - number of vertices, k - number of edges
    edges = defaultdict(list)
    is_visited = defaultdict(lambda: False)

    for i in range(k):
        f, s = map(int, input().split())
        edges[f].append(s)
        edges[s].append(f)

    for i in range(1, n + 1):
        if(not is_visited[i]):
            for j in edges[i]:
                is_visited[j] = True

            for j in edges[i]:
                for k in edges[j]:
                    is_visited[k] = True

    for i in range(1, n + 1):
        if(not is_visited[i]):
            print(i)

if __name__ == "__main__":
    main()
