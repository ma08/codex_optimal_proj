import sys
sys.setrecursionlimit(10**6)


def dfs(start, visited, dist):
    global min_dist
    if len(visited) == k:
        min_dist = min(min_dist, dist)
        return
    for nxt in tiles[start]:
        if nxt in visited:
            continue
        visited.add(nxt)
        dfs(nxt, visited, dist+abs(nxt[0]-start[0])+abs(nxt[1]-start[1]))
        visited.remove(nxt)

def main():
    n, k = map(int, sys.stdin.readline().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    tiles = [[] for _ in range(k+1)]
    for i in range(n):
        for j in range(n):
            tiles[matrix[i][j]].append((i, j))
    min_dist = float('inf')
    for start in tiles[1]: # start is (r, c)
        dfs(start, set([start]), 0)
    if min_dist == sys.maxsize:
        print(-1)
    else:
        print(min_dist)

if __name__ == "__main__":
    main()
