
import sys
sys.setrecursionlimit(10**7)

def dfs(v, p, g):
    if p == -1:
        g[v][v] = 0
    else:
        g[v][v] = g[p][v]

    for i in range(len(g)):
        if i != v and i != p:
            g[v][i] = g[v][v] + g[v][i]

    for i in range(len(g)):
        if i != v and i != p:
            dfs(i, v, g)


def main():
    n = int(input())
    g = []
    for i in range(n):
        g.append(list(map(int, input().split())))

    if h % 3 == 0 or w % 3 == 0:
        print(0)
        return

    if h > w:
        h, w = w, h

    min_diff = float('inf')
    for i in range(1, h):
        area_1 = i * w
        area_2 = (h - i) // 2 * w
        area_3 = (h - i) - area_2
        max_area = max(area_1, area_2, area_3)
        min_area = min(area_1, area_2, area_3)
        min_diff = min(min_diff, max_area - min_area)

    print(min_diff)


if __name__ == '__main__':
    main()
