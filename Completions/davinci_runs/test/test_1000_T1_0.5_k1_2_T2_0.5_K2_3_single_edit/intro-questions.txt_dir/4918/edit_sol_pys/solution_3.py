
import sys

def find(a):
    if parent[a] == a:
        return a
    else:
        return find(parent[a])

def union(a, b):
    root1 = find(a)
    root2 = find(b)
    if root1 != root2:
        parent[root2] = root1

def main():
    n, q = map(int, sys.stdin.readline().split())
    parent = [i for i in range(n+1)]
    for _ in range(q):
        line = sys.stdin.readline().split()
        if line[0] == 't':
            union(int(line[1]), int(line[2]))
        elif line[0] == 's':
            print(size[parent[int(line[1])]])
            size[parent[int(line[1])]] += 1

if __name__ == '__main__':
    main()
