
# this is a comment
import sys

def find(a):
    # find root of a
    if parent[a] == a:
        return a
    else:
        return find(parent[a])

def union(a, b):
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
            print(parent.count(find(int(line[1]))))

if __name__ == '__main__':
    main()
