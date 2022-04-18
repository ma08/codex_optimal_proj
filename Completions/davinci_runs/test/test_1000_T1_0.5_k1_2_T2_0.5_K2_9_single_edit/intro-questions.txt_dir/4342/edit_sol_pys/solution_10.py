
def main():
    # n = int(input())
    # a = list(map(int, input().split()))
    # edges = []
    # for i in range(n-1):
    #     v, u = map(int, input().split())
    #     edges.append((v, u))
    n = 5
    a = [2, 0, 0, 1, 2]
    edges = [(1, 2), (2, 3), (2, 4), (2, 5)]
    # n = 5
    # a = [1, 0, 0, 0, 2]
    # edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
    # n = 3
    # a = [1, 1, 2]
    # edges = [(2, 3), (1, 3)]
    # n = 4
    # a = [1, 1, 1, 1]
    # edges = [(1, 2), (2, 3), (3, 4)]
    # n = 2
    # a = [1, 1]
    # edges = [(1, 2)]
    # n = 4
    # a = [1, 1, 1, 1]
    # edges = [(1, 2), (2, 3), (3, 4)]
    nice_edges = 0
    for i in range(n-1):
        v, u = edges[i]
        if a[v-1] == 0 or a[u-1] == 0:
            nice_edges += 1
    print(nice_edges)

if __name__ == '__main__':
    main()
