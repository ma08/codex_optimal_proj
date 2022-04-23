

def check_square(tiles, square):
    for i in range(len(square)):
        for j in range(len(square)):
            if square[i][j] == 0:
                for tile in tiles:
                    if check_tile(tiles[tile], square, i, j):
                        square[i][j] = tiles[tile][0][0]
                        square[i][j+1] = tiles[tile][0][1]
                        square[i+1][j] = tiles[tile][1][0]
                        square[i+1][j+1] = tiles[tile][1][1]
                        break
                else:

                    return False
    return True

    if i+1 >= len(square) or j+1 >= len(square):
        return False

    if square[i][j] == 0 and square[i][j+1] == 0 and square[i+1][j] == 0 and square[i+1][j+1] == 0:
        if square[i][j+1] == tile[0][0] and square[i+1][j+1] == tile[1][0] and square[i+1][j] == tile[0][1] and square[i][j] == tile[1][1]:
            return True
        if square[i+1][j] == tile[0][0] and square[i+1][j+1] == tile[1][0] and square[i][j+1] == tile[0][1] and square[i][j] == tile[1][1]:
            return True
        if square[i][j] == tile[0][0] and square[i][j+1] == tile[1][0] and square[i+1][j+1] == tile[0][1] and square[i+1][j] == tile[1][1]:
            return True
        if square[i][j] == tile[0][0] and square[i+1][j] == tile[1][0] and square[i][j+1] == tile[0][1] and square[i+1][j+1] == tile[1][1]:
            return True

    return False


def main():
    cases = int(input())
    for case in range(cases):
        n, m = map(int, input().split())
        tiles = []
        for i in range(n):
            tiles.append([list(map(int, input().split())) for i in range(2)])
        square = [[0 for i in range(m*2)] for j in range(m*2)]
        if check_square(tiles, square):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
