

def check_square(tiles, board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                for tile in tiles:
                    if check_tile(tile, board, i, j):
                        board[i][j] = tile[0][0]
                        board[i][j+1] = tile[0][1]
                        board[i+1][j] = tile[1][0]
                        board[i+1][j+1] = tile[1][1]
                        break
                else:
                    return False
    return True

    # if board[i][j] == 0 and board[i][j+1] == 0 and board[i+1][j] == 0 and board[i+1][j+1] == 0:
    #     if i+1 < len(board) and j+1 < len(board):
    #         if board[i][j+1] == tile[0][0] and board[i+1][j+1] == tile[1][0] and board[i+1][j] == tile[0][1] and board[i][j] == tile[1][1]:
    #             return True
    #         if board[i+1][j] == tile[0][0] and board[i+1][j+1] == tile[1][0] and board[i][j+1] == tile[0][1] and board[i][j] == tile[1][1]:
    #             return True
    #         if board[i][j] == tile[0][0] and board[i][j+1] == tile[1][0] and board[i+1][j+1] == tile[0][1] and board[i+1][j] == tile[1][1]:
    #             return True
    #         if board[i][j] == tile[0][0] and board[i+1][j] == tile[1][0] and board[i][j+1] == tile[0][1] and board[i+1][j+1] == tile[1][1]:
    #             return True
    # return False

def main():
    cases = int(input())
    for case in range(cases):
        n, m = map(int, input().split())
        tiles = []
        for i in range(n):
            tiles.append([list(map(int, input().split())) for i in range(2)])
        board = [[0 for i in range(m)] for j in range(m)]
        if check_square(tiles, board):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
