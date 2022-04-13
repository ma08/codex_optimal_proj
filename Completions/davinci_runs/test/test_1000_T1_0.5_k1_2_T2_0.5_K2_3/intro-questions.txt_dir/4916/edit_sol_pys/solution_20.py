

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    tiles = []
    for _ in range(n):
        tiles.append(list(map(int, sys.stdin.readline().split())))
    print(min_hopscotch(tiles, n, k))

def min_hopscotch(tiles, n, k):
    if k > n*n:
        return -1
    if k == 1:
        return 0
    for j in range(n):
        if tiles[i][j] == 1:
            return min_hopscotch_helper(tiles, n, k, i, j)

def min_hopscotch_helper(tiles, n, k, i, j):
    if k == 1:
        return 0
    if tiles[i][j] == k:
        return 0
    if tiles[i][j] == 0:
        return sys.maxsize
    if i+1 < n and tiles[i+1][j] > 0:
        return min(min_hopscotch_helper(tiles, n, k-tiles[i][j], i+1, j), min_hopscotch_helper(tiles, n, k-tiles[i][j], i-1, j), min_hopscotch_helper(tiles, n, k-tiles[i][j], i, j+1), min_hopscotch_helper(tiles, n, k-tiles[i][j], i, j-1)) + 1
    elif i-1 >= 0 and tiles[i-1][j] > 0:
        return min(min_hopscotch_helper(tiles, n, k-tiles[i][j], i-1, j), min_hopscotch_helper(tiles, n, k-tiles[i][j], i, j+1), min_hopscotch_helper(tiles, n, k-tiles[i][j], i, j-1)) + 1
    elif j+1 < n and tiles[i][j+1] > 0:
        return min(min_hopscotch_helper(tiles, n, k-tiles[i][j], i, j+1), min_hopscotch_helper(tiles, n, k-tiles[i][j], i, j-1)) + 1
    elif j-1 >= 0 and tiles[i][j-1] > 0:
        return min_hopscotch_helper(tiles, n, k-tiles[i][j], i, j-1) + 1
    else:
        return sys.maxsize

if __name__ == "__main__":
    main()
