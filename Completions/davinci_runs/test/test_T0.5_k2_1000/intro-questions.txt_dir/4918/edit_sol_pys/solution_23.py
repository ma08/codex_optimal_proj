

def find(node, parents):
    if node != parents[node]:
        parents[node] = find(parents[node], parents)
    return parents[node]

def merge(node1, node2, parents, size):
    root1 = find(node1, parents)
    root2 = find(node2, parents)
    if root1 == root2:
        return
    if size[root1] < size[root2]:
        root1, root2 = root2, root1
    parents[root2] = root1
    size[root1] += size[root2]

def main():
    n, q = map(int, input().split())
    parents = [i for i in range(n + 1)]
    size = [1 for i in range(n + 1)]
    for _ in range(q):
        query = input().split()
        if query[0] == 't':
            merge(int(query[1]), int(query[2]), parents, size)
        else:
            print(size[find(int(query[1]), parents)])

if __name__ == "__main__":
    main()
