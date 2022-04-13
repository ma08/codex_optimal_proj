
import sys

def find(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find(x)] = find(y)

def main():
    n, q = map(int, sys.stdin.readline().split())
    global p
    p = [i for i in range(n)]
    for i in range(q):
        line = sys.stdin.readline().strip().split()
        if line[0] == 'u':
            union(int(line[1]), int(line[2]))
        else:
            print(p.count(find(int(line[1]))))

if __name__ == '__main__':
    main()
