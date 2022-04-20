

import itertools

def is_path(path, edges):
    for i in range(len(path)-1):
        if (path[i], path[i+1]) not in edges and (path[i+1], path[i]) not in edges:
            return False
    return True

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))
    paths = itertools.permutations(range(2, n+1))
    cnt = 0
    for path in paths:
        if is_path((1,) + path, edges):
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()