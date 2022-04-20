

def perm(n, k, l):
    if k == 1:
        yield [l[0]]
    else:
        for i in range(k):
            for ss in perm(n, k-1, l[:i] + l[i+1:]):
                yield [l[i]] + ss

def comb(n, k):
    return perm(n, k, [i for i in range(1, n+1)])

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))

    tree_edges = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i < j and (i, j) not in edges:
                tree_edges.append((i, j))
    tree_edges = list(set(tree_edges))

    pathes = []
    for c in comb(n-1, n-1):
        pathes.append(c)

    for p in pathes:
        for i in range(1, len(p)):
            if (p[i-1], p[i]) not in tree_edges:
                pathes.remove(p)
                break

    print(len(pathes))

if __name__ == '__main__':
    main()