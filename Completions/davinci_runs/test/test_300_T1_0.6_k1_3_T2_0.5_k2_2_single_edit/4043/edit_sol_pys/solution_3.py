

def generate_graph(n, d, k):
    if d > n:
        return float("inf")

    if d == 1:
        if k >= n - 1:
            return [1 for i in range(n - 1)]
        else:
            return float("inf")

    if d == 2:
        if k >= n - 1:
            return [1 for i in range(n - 1)]
        elif k >= 2:
            return [1, 2]
        else:
            return float("inf")

    if d == 3:
        if k >= n - 1:
            return [1 for i in range(n - 1)]
        elif k >= 4:
            return [1, 2, 3, 3, 4, 5]
        else:
            return float("inf")

    if d == 4:
        if k >= n - 1:
            return [1 for i in range(n - 1)]
        elif k >= 3:
            return [1, 2, 3, 4, 5, 6]
        else:
            return float("inf")

    if k >= 4:
        return [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11]

    return float("inf")

def main():
    n, d, k = readl()
    graph = generate_graph(n, d, k)
    if graph == float("inf"):
        return

    print "YES"
    for i in range(1, n):
        print(i, graph[i - 1])

if __name__ == '__main__':
    main()
