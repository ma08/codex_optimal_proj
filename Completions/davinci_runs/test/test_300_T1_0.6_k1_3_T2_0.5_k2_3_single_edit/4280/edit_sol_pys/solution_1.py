
import sys

def dfs(u, edges, colors, curr_color):
    colors[u] = curr_color
    for i in edges[u]:
        if colors[i] == 0:
            dfs(i, edges, colors, curr_color)


def main():
    n, k = map(int, sys.stdin.readline().split())
    edges = {}
    for i in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        if a in edges:
            edges[a].append(b)
        else:
            edges[a] = [b]
        if b in edges:
            edges[b].append(a)
        else:
            edges[b] = [a]
    colors = [0]*(n+1)
    curr_color = 1
    for i in range(1, n+1):
        if colors[i] == 0:
            dfs(i, edges, colors, curr_color)
            curr_color += 1
    print(curr_color-1)
    for i in range(1, n):
        print(colors[i])


if __name__ == "__main__":
    main()
