

import sys


def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    if m == 0:
        print(0)
        return
    edges = [[int(x) for x in sys.stdin.readline().split()] for i in range(m)]
    edges.sort(key=lambda x: x[2])
    # print(edges)
    d = [0] * n
    for i in range(1, n):
        d[i] = sys.maxsize
    for i in range(m):
        if d[edges[i][1]] > d[edges[i][0]] + edges[i][2]:
            d[edges[i][1]] = d[edges[i][0]] + edges[i][2]
    # print(d)
    for i in range(m):
        if d[edges[i][1]] > d[edges[i][0]] + edges[i][2]:
            print('-')
            return
    print(d[n - 1])


main()
