

def check_square(tiles, square):
    for i in range(len(square)):
        for j in range(len(square)):
            if square[i][j] == 0:
                if not check_tile(tiles, square, i, j):
                    return False 
    return True

    for tile in tiles:
        if check_tile(tile, square, i, j):
            square[i][j] = tile[0][0]
            square[i][j+1] = tile[0][1]
            square[i+1][j] = tile[1][0]
            square[i+1][j+1] = tile[1][1]
            return True
    else:
        return False

def check_tile(tiles, square, i, j):
    if square[i][j] == 0 and square[i][j+1] == 0 and square[i+1][j] == 0 and square[i+1][j+1] == 0:
        if i+1 < len(square) and j+1 < len(square):
            for tile in tiles:
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
        square = [[0 for i in range(m)] for j in range(m)]
        if check_square(tiles, square):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
