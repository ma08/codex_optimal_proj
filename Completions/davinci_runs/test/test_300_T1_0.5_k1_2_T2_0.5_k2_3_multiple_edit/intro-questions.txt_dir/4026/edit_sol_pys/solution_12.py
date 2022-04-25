

def check_square(tiles, square, n, m):
    for i in range(len(square)):
        for j in range(len(square)):
            if square[i][j] == 0:
                for tile in tiles: # check if the tile is valid
                    if check_tile(tile, square, i, j, n, m):
                        square[i][j] = tile[0][0] # insert tile
                        square[i][j+1] = tile[0][1] # insert tile
                        square[i+1][j] = tile[1][0] # insert tile
                        square[i+1][j+1] = tile[1][1] # insert tile
                        break
                else:
                    return False
    return True

    if i+1 >= len(square) or j+1 >= len(square): # check if the tile fits
        return False
    if square[i][j] == 0 and square[i][j+1] == 0 and square[i+1][j] == 0 and square[i+1][j+1] == 0: # check if the tile is valid
        if square[i][j+1] == tile[0][0] and square[i+1][j+1] == tile[1][0] and square[i+1][j] == tile[0][1] and square[i][j] == tile[1][1]: # check if the tile is valid
            return True # the tile is valid
        if square[i+1][j] == tile[0][0] and square[i+1][j+1] == tile[1][0] and square[i][j+1] == tile[0][1] and square[i][j] == tile[1][1]: # check if the tile is valid
            return True # the tile is valid
        if square[i][j] == tile[0][0] and square[i][j+1] == tile[1][0] and square[i+1][j+1] == tile[0][1] and square[i+1][j] == tile[1][1]: # check if the tile is valid
            return True # the tile is valid
        if square[i][j] == tile[0][0] and square[i+1][j] == tile[1][0] and square[i][j+1] == tile[0][1] and square[i+1][j+1] == tile[1][1]: # check if the tile is valid
            return True # the tile is valid
    return False # the tile is invalid

def main():
    cases = int(input())
    for case in range(cases):
        n, m = map(int, input().split())
        tiles = []
        for i in range(n):
            tiles.append([list(map(int, input().split())) for i in range(2)])
        square = [[0 for i in range(m)] for j in range(m)]
        if check_square(tiles, square, n, m):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
