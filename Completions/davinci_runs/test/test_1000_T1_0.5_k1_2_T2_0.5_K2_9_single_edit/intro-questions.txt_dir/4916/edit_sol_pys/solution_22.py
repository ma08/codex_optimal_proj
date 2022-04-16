


import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    tiles = [[] for _ in range(k+1)]
    for i in range(n):
        for j in range(n):
            tiles[matrix[i][j]].append((i, j))
    min_dist = sys.maxsize
    for start in tiles[1]:
        visited = set()
        visited.add(start)
        dist = 0
        for i in range(2, k+1):
            curr_dist = sys.maxsize
            for tile in tiles[i]:
                if tile in visited:
                    continue
                dist = abs(start[0]-tile[0]) + abs(start[1]-tile[1])
                curr_dist = min(dist, curr_dist)
            if curr_dist == sys.maxsize:
                break
            dist += curr_dist
            visited.add(tile)
            start = tile
        if len(visited) == k:
            min_dist = min(min_dist, dist)
    if min_dist == sys.maxsize:
        print(-1)
    else:
        print(min_dist)

if __name__ == "__main__":
    main()
