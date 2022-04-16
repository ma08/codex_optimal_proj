import sys
sys.setrecursionlimit(10**6)


def dfs(x, y, G, visited):
    visited[x][y] = True
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= h or ny >= w:
            continue
        if G[nx][ny] == "#" and visited[nx][ny] == False:
            dfs(nx, ny, G, visited)


def main():
    h, w = map(int, input().split())
    G = [input() for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if G[i][j] == "#" and visited[i][j] == False:
                dfs(i, j, G, visited)
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()
