

import sys
from collections import defaultdict

def build_tiles():
    tiles = defaultdict(list)
    n = int(input())
    m = int(input())
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        c, d = [int(x) for x in input().split()]
        tiles[(a,b)].append((c,d))
        tiles[(c,d)].append((a,b))
    return tiles

def build_matrix(tiles, m):
    matrix = [[-1 for _ in range(m)] for _ in range(m)]
    i, j = 0, 0
    while i < m:
        if matrix[i][j] != -1:
            i += 1
            j = 0
            continue
        a, b = tiles[(i,j)]
        if matrix[a][b] != -1:
            return None
        matrix[i][j] = matrix[j][i] = 0
        matrix[a][b] = matrix[b][a] = 0
        j += 1
    return matrix

def solve():
    tiles = build_tiles()
    m = build_matrix(tiles, max(tiles.keys())[0]+1)
    if m:
        return "YES"
    else:
        return "NO"

def main():
    t = int(input())
    for i in range(t):
        print(solve())

if __name__ == "__main__":
    sys.exit(main())
