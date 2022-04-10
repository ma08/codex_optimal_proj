

def main():
    # read input
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        tiles = [[0, 0, 0, 0] for _ in range(n)]
        for i in range(n):
            tiles[i][0], tiles[i][1] = map(int, input().split())
            tiles[i][2], tiles[i][3] = map(int, input().split())
        # check if tiles can be used to construct square
        print("YES" if check(tiles, m) else "NO")

def check(tiles, m):
    # check if tiles can be used to construct square
    return False

if __name__ == "__main__":
    main()