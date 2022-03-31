

from collections import defaultdict

def dfs_topsort(graph):
    visited = [False]*len(graph)
    top_sort = []

    def dfs(node):
        visited[node] = True
        for n in graph[node]:
            if not visited[n]:
                dfs(n)
        top_sort.append(node)

    for node in range(len(graph)):
        if not visited[node]:
            dfs(node)

    return top_sort[::-1]


def main():
    n = int(input())
    words = [input() for _ in range(n)]

    graph = defaultdict(list)
    for i, word in enumerate(words):
        for j, other in enumerate(words):
            if i == j:
                continue
            if word in other:
                graph[i].append(j)

    try:
        top_sort = dfs_topsort(graph)
    except:
        print("NO")
        return

    print("YES")
    for i in top_sort:
        print(words[i])


if __name__ == "__main__":
    main()
