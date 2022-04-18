import sys
import time

def find(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p1 = find(x)
    p2 = find(y)
    if p1 != p2:
        p[p1] = p2

def q1(n, q):
    p = [i for i in range(n+1)]
    for i in range(q):
        line = sys.stdin.readline().strip().split()
        if line[0] == 't':
            union(int(line[1]), int(line[2]))
        else:
            print(p.count(find(int(line[1]))))

def main():
    n, q = map(int, sys.stdin.readline().split())
    t = time.time()
    q1(n, q)
    print(time.time() - t)

if __name__ == '__main__':
    main()
