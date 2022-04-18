

def find(node, parent):
    if node != parent[node]:
        parent[node] = find(parent[node], parent)
    return parent[node]

def union(node1, node2, parent, size, count):
    root1 = find(node1, parent)
    root2 = find(node2, parent)
    if root1 == root2:
        return
    if size[root1] < size[root2]:
        root1, root2 = root2, root1
    parent[root2] = root1
    count[0] -= 1
    size[root1] += size[root2]

def main():
    n, q = map(int, input().split())
    parent = [i for i in range(n + 1)]
    size = [1 for i in range(n + 1)]
    count = [n]
    for _ in range(q):
        query = input().split()
        if query[0] == 't':
            union(int(query[1]), int(query[2]), parent, size, count)
        else:
            print(count[0])

if __name__ == "__main__":
    main()
