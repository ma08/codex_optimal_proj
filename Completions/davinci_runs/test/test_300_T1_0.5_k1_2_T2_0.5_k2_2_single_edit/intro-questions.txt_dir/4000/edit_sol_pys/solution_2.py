

def main():
    pass

def path(tree, a, b, c, i):
    if i == 0:
        return find_path(tree, a, b)
    elif i == 1:
        return find_path(tree, b, c)
    else:
        return find_path(tree, a, c)

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
