import sys

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    p1 = find(x)
    p2 = find(y)
    if p1 != p2:
        parent[p1] = p2

def main():
    n, q = map(int, sys.stdin.readline().split())
    global parent
    parent = [i for i in range(n+1)]
    for i in range(q):
        line = sys.stdin.readline().strip().split()
        if line[0] == 'u':
            union(int(line[1]), int(line[2]))
        else:
            print(parent.count(find(int(line[1]))))

if __name__ == '__main__':
    main()
