
def find(parent, node):
    if node != parent[node]:
        parent[node] = find(parent, parent[node])
    return parent[node]

def merge(node1, node2, parent, size):
    root1 = find(parent, node1)
    root2 = find(parent, node2)
    if root1 == root2:
        return
    if size[root1] < size[root2]:
        root1, root2 = root2, root1
    parent[root2] = root1
    size[root1] += size[root2]

def main():
    n, q = map(int, input().split())
    parent = [i for i in range(n + 1)]
    size = [1 for i in range(n + 1)]
    for _ in range(q):
        query = input().split()
        if query[0] == 't':
            merge(int(query[1]), int(query[2]), parent, size)
        else:
            print(size[find(parent, int(query[1]))])

if __name__ == "__main__":
    main()
