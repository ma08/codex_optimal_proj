
def main():
    n = int(input())
    tree = [[] for i in range(n)]
    for i in range(n-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    for i in range(n):
        tree[i].sort()
    max_path = 0
    for i in range(n):
        for j in range(len(tree[i])):
            for k in range(j+1, len(tree[i])):
                a, b, c = i+1, tree[i][j]+1, tree[i][k]+1
                path = [0]*3
                for l in range(3):
                    path[l] = len(find_path(tree, a, b, c, l))
                max_path = max(max_path, sum(path))
                if max_path == sum(path):
                    ans = [a, b, c]
    print(max_path)
    print(*ans)

def find_path(tree, a, b, c, i):
    if i == 0:
        return bfs(tree, a, b)
    elif i == 1:
        return bfs(tree, b, c)
    else:
        return bfs(tree, a, c)

def bfs(tree, a, b):
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
