

def check_square(tiles, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                for tile in tiles:
                    if i+1 < len(matrix) and j+1 < len(matrix):
                        if matrix[i][j+1] == tile[0][0] and matrix[i+1][j+1] == tile[1][0] and matrix[i+1][j] == tile[0][1] and matrix[i][j] == tile[1][1]:
                            matrix[i][j] = tile[0][0]
                            matrix[i][j+1] = tile[0][1]
                            matrix[i+1][j] = tile[1][0]
                            matrix[i+1][j+1] = tile[1][1]
                            break
                        if matrix[i+1][j] == tile[0][0] and matrix[i+1][j+1] == tile[1][0] and matrix[i][j+1] == tile[0][1] and matrix[i][j] == tile[1][1]:
                            matrix[i][j] = tile[0][0]
                            matrix[i][j+1] = tile[0][1]
                            matrix[i+1][j] = tile[1][0]
                            matrix[i+1][j+1] = tile[1][1]
                            break
                        if matrix[i][j] == tile[0][0] and matrix[i][j+1] == tile[1][0] and matrix[i+1][j+1] == tile[0][1] and matrix[i+1][j] == tile[1][1]:
                            matrix[i][j] = tile[0][0]
                            matrix[i][j+1] = tile[0][1]
                            matrix[i+1][j] = tile[1][0]
                            matrix[i+1][j+1] = tile[1][1]
                            break
                        if matrix[i][j] == tile[0][0] and matrix[i+1][j] == tile[1][0] and matrix[i][j+1] == tile[0][1] and matrix[i+1][j+1] == tile[1][1]:
                            matrix[i][j] = tile[0][0]
                            matrix[i][j+1] = tile[0][1]
                            matrix[i+1][j] = tile[1][0]
                            matrix[i+1][j+1] = tile[1][1]
                            break
                return False
    return True

def main():
    cases = int(input())
    for case in range(cases):
        n, m = map(int, input().split())
        tiles = []
        for i in range(n):
            tiles.append([list(map(int, input().split())) for i in range(2)])
        matrix = [[0 for i in range(m)] for j in range(m)]
        if check_square(tiles, matrix):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
