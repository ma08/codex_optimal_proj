
import sys

def build_square(tiles):
    for tile in tiles:
        if tile[0][0] != tile[0][1]:
            return False

    return True


if __name__ == "__main__":
    t = int(sys.stdin.readline())

    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        tiles = []

        for _ in range(n):
            tiles.append([list(map(int, sys.stdin.readline().split())),
                          list(map(int, sys.stdin.readline().split()))])

        print("YES" if build_square(tiles) else "NO")
