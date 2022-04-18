import sys
sys.setrecursionlimit(10**6)

def find(node, parent):
    if node != parent[node]:
        parent[node] = find(parent[node], parent)
    return parent[node]

def merge(node1, node2, parent, size):
    root1 = find(node1, parent)
    root2 = find(node2, parent)
    if root1 == root2:
        return
    if size[root1] < size[root2]:
        root1, root2 = root2, root1
    parent[root2] = root1
    size[root1] += size[root2]

def main():
    n, q = map(int, sys.stdin.readline().split())
    parent = [i for i in range(n + 1)]
    size = [1 for i in range(n + 1)]
    for _ in range(q):
        query = sys.stdin.readline().split()
        if query[0] == 't':
            merge(int(query[1]), int(query[2]), parent, size)
        else:
            print(size[find(int(query[1]), parent)])

if __name__ == "__main__":
    main()
