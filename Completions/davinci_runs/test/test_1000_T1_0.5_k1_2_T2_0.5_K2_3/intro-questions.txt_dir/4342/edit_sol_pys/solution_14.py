import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    edges = []
    for i in range(n-1):
        v, u = map(int, sys.stdin.readline().split())
        edges.append((v, u))
    nice_edges = 0
    for i in range(n-1):
        v, u = edges[i]
        if a[v-1] == 0 or a[u-1] == 0:
            nice_edges += 1
    print(nice_edges)

if __name__ == '__main__':
    main()
