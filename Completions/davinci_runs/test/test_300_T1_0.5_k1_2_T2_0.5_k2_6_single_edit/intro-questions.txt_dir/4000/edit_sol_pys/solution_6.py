

def main():
    n = int(input())
    tree = [[] for i in range(n)]
    for i in range(n-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    for i in range(n):
        tree[i].sort()
    max_paths = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                a, b, c = i+1, j+1, k+1
                pa, pb, pc = path(tree, a, b, c)
                max_paths = max(max_paths, len(pa)+len(pb)+len(pc))
                if max_paths == len(pa)+len(pb)+len(pc):
                    ans = [a, b, c, len(pa), len(pb), len(pc)]
    print(max_paths)
    print(*ans, sep=' ')

def path(tree, a, b, c):
    return find_path(tree, a, b), find_path(tree, b, c), find_path(tree, a, c)

def find_path(tree, a, b):
    q = [a-1]
    visited = [False]*len(tree)
    visited[a-1] = True
    while q:
        cur = q.pop(0)
        if cur == b-1:
            return visited
        for node in tree[cur]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
    return []

main()
