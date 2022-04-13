
def main():
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n):
        v, u = map(int, input().split())
        edges.append((v, u))
    nice_edges = 0
    for i in range(n):
        v, u = edges[i]
        if a[v-1] == 0 or a[u-1] == 0:
            nice_edges += 1
    print(nice_edges)

if __name__ == '__main__':
    main()
