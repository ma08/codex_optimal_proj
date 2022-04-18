
import sys
from collections import defaultdict

def find(a, parent):
    # find root of a
    while parent[a] != a:
        a = parent[a]
    return a

def union(a, b, parent):
    # union of two sets
    root1 = find(a)
    root2 = find(b)
    if root1 != root2:
        parent[root2] = root1

def main():
    global parent
    n, q = map(int, sys.stdin.readline().split())
    parent = [i for i in range(n+1)]
    for _ in range(q):
        line = sys.stdin.readline().split()
        if line[0] == 't':
            union(int(line[1]), int(line[2]))
        elif line[0] == 's':
            print(parent[find(int(line[1]))])

if __name__ == '__main__':
    main()
