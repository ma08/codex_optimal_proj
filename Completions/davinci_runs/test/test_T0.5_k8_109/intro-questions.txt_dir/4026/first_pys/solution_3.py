

def main():
    t = int(input())
    for _ in range(t):
        n,m = [int(x) for x in input().split()]
        tiles = []
        for _ in range(n):
            tiles.append([int(x) for x in input().split()] + [int(x) for x in input().split()])
        if is_possible(tiles,m):
            print("YES")
        else:
            print("NO")

def is_possible(tiles,m):
    for i in range(m):
        for j in range(m):
            for k in range(len(tiles)):
                if tiles[k][0] == i and tiles[k][1] == j:
                    if tiles[k][2] == i and tiles[k][3] == j:
                        return False
                    if tiles[k][2] == m-j-1 and tiles[k][3] == m-i-1:
                        return False
    return True

if __name__ == "__main__":
    main()