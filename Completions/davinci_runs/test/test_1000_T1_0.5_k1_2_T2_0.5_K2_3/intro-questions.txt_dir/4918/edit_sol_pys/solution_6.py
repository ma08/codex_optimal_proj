

def find(n, parent):
    if n != parent[n]:
        parent[n] = find(parent[n], parent)
    return parent[n]

def merge(n1, n2, parent, size):
    root1 = find(n1, parent)
    root2 = find(n2, parent)
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
            print(size[find(int(query[1]), parent)])

if __name__ == "__main__":
    main()
