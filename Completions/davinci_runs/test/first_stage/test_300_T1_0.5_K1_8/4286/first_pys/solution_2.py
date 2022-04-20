

import sys

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    a = [int(x) for x in sys.stdin.readline().split()]
    offers = {}
    for i in range(m):
        x, y, w = [int(x) for x in sys.stdin.readline().split()]
        if (x, y) not in offers:
            offers[(x, y)] = w
        else:
            offers[(x, y)] = min(offers[(x, y)], w)
        if (y, x) not in offers:
            offers[(y, x)] = w
        else:
            offers[(y, x)] = min(offers[(y, x)], w)

    groups = []
    for i in range(n):
        groups.append([i])

    def find(x):
        for g in groups:
            if x in g:
                return g
        return None

    def union(g1, g2):
        g = g1 + g2
        groups.remove(g1)
        groups.remove(g2)
        groups.append(g)

    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) in offers:
                g1 = find(i)
                g2 = find(j)
                if g1 != g2:
                    union(g1, g2)

    cost = 0
    for g in groups:
        g_cost = 10**18
        for i in range(len(g)):
            for j in range(i + 1, len(g)):
                if (g[i], g[j]) in offers:
                    g_cost = min(g_cost, offers[(g[i], g[j])])
                else:
                    g_cost = min(g_cost, a[g[i]] + a[g[j]])
        cost += g_cost
    print(cost)

if __name__ == "__main__":
    main()