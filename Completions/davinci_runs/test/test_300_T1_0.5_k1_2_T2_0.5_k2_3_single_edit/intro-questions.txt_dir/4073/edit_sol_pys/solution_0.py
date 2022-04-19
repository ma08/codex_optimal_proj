

def main():
    """
    This is the main function.
    """

    # Read the input data
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]

    # Solve the problem
    visited = set()
    queue = [1]
    visited.add(1)

    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)

    # Print the solution
    print(len(visited) - 1)

if __name__ == "__main__":
    main()
