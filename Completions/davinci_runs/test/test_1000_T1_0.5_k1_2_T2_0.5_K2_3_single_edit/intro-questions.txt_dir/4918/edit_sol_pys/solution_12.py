
import sys

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    p1 = find(x)
    p2 = find(y)
    if p1 != p2 and rank[p1] < rank[p2]:
        parent[p1] = p2
    elif p1 != p2 and rank[p1] > rank[p2]:
        parent[p2] = p1
    elif p1 != p2 and rank[p1] == rank[p2]:
        parent[p1] = p2
        rank[p2] += 1

def main():
    n, q = map(int, sys.stdin.readline().split())
    global parent
    global rank
    parent = [i for i in range(n+1)]
    rank = [1] * (n+1)
    for i in range(q):
        line = sys.stdin.readline().strip().split()
        if line[0] == 't':
            union(int(line[1]), int(line[2]))
        else:
            print(parent.count(find(int(line[1]))))

if __name__ == '__main__':
    main()
