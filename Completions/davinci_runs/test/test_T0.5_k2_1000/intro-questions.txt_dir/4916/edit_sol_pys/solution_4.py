
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    tiles = []
    for _ in range(n):
        tiles.append(list(map(int, sys.stdin.readline().split())))
    print(min_hopscotch(tiles, n, k))

def min_hopscotch(tiles, n, k):
    if k == 1:
        return 0
    for i in range(n):
        for j in range(n):
            if tiles[i][j] == 1:
                return min_hopscotch_helper(tiles, n, k, i, j)
    return -1

def min_hopscotch_helper(tiles, n, k, i, j):
    if i < 0 or j < 0 or i >= n or j >= n:
        return -1
    if tiles[i][j] == k:
        return 0
    if tiles[i][j] == 0 or tiles[i][j] > k:
        return -1
    return min(min_hopscotch_helper(tiles, n, k, i+1, j), min_hopscotch_helper(tiles, n, k, i-1, j), min_hopscotch_helper(tiles, n, k, i, j+1), min_hopscotch_helper(tiles, n, k, i, j-1)) + 1

if __name__ == "__main__":
    main()
