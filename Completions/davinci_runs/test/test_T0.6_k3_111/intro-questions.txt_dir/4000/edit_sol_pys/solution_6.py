

import sys
import queue

def bfs(tree, root, visited):
    visited[root] = True
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        curr = q.get()
        for neighbor in tree[curr]:
            if not visited[neighbor]:
                q.put(neighbor)
                visited[neighbor] = True

def get_connected_components(tree, n):
    visited = [False] * (n + 1)
    cc = 0
    for i in range(1, n + 1):
        if not visited[i]:
            bfs(tree, i, visited)
            cc += 1
    return cc

def main():
    nextint = iter(map(int, sys.stdin.read().split())).__next__()
    n = nextint()
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = nextint(), nextint()
        tree[a].append(b)
        tree[b].append(a)
    # No need to check if the input is a tree, since it's guaranteed to be a tree
    cc = get_connected_components(tree, n)
    if cc == 1:
        res = n - 1
        a = 1
        b = 2
        c = 3
    elif cc == 2:
        res = n - 2
        a = b = c = 1
    else:
        res = n - 3
        a = b = 1
        c = 2
    print(res)
    print('{} {} {}'.format(a, b, c))

if __name__ == '__main__':
    main()
