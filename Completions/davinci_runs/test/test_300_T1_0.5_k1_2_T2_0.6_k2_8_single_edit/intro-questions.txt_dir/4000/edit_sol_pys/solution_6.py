

def main():
    n = int(input())
    tree = [[] for i in range(n)]
    for i in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    for i in range(n):
        tree[i].sort()
    max_paths = 0
    for i in range(n):
        for j in range(len(tree[i])):
            for k in range(j+1, len(tree[i])):
                a, b, c = i+1, tree[i][j], tree[i][k]
                paths = [0]*3
                for l in range(3):
                    paths[l] = len(path(tree, a, b, c, l))
                max_paths = max(max_paths, sum(paths))
                if max_paths == sum(paths):
                    ans = [a, b, c]
    print(max_paths)
    print(*ans)

def path(tree, a, b, c, i):
    if i == 0:
        return find_path(tree, a, b)
    elif i == 1:
        return find_path(tree, b, c)
    else:
        return find_path(tree, a, c)

def find_path(tree, a, b):
    q = [a]
    visited = [False]*len(tree)
    visited[a] = True
    while q:
        cur = q.pop(0)
        if cur == b:
            return visited
        for node in tree[cur]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
    return []

main()
