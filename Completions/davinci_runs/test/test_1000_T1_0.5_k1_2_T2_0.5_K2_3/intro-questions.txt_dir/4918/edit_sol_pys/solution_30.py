
def find(n, p):
    if n != p[n]:
        p[n] = find(p[n], p)
    return p[n]

def merge(n1, n2, p, size):
    root1 = find(n1, p)
    root2 = find(n2, p)
    if root1 == root2:
        return
    if size[root1] < size[root2]:
        root1, root2 = root2, root1
    p[root2] = root1
    size[root1] += size[root2]

def main():
    n, q = map(int, input().split())
    p = [i for i in range(n)]
    size = [1 for i in range(n)]
    for _ in range(q):
        query = input().split()
        if query[0] == 't':
            merge(int(query[1]), int(query[2]), p, size)
        else:
            print(size[find(int(query[1]), p)])

if __name__ == "__main__":
    main()
