
import sys

def find(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p1 = find(x)
    p2 = find(y)
    if p1 != p2:
        p[p1] = p2

def main():
    n, q = map(int, sys.stdin.readline().split())
    global p
    p = [i for i in xrange(n+1)]
    for i in range(q):
        line = sys.stdin.readline().strip().split()
        if line[0] == 't':
            union(int(line[1]), int(line[2]))
        else:
            print(p.count(find(int(line[1]))))

if __name__ == '__main__':
    main()
