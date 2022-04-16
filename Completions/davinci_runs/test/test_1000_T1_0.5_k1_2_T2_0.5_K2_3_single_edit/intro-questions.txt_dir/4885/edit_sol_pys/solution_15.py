
# Solution:
import sys


def main():
    board = []
    for i in range(8):
        board.append(list(input()))
    for i in range(8):
        board.append(list(input()))
    pieces = {"K": [], "Q": [], "R": [], "B": [], "N": [], "P": []}
    for i in range(8):
        for j in range(8):
            if board[i][j] != ":":
                pieces[board[i][j]].append((i, j))
    white = "White: "
    black = "Black: "
    for piece in "KQRBNP":
        for pos in pieces[piece]:
            if pos[0] < 8:
                white += piece + chr(ord("a") + pos[1]) + str(8 - pos[0]) + ","
            else:
                black += piece + chr(ord("a") + pos[1]) + str(8 - pos[0]) + ","
    print(white[:-1])
    print(black[:-1])


if __name__ == "__main__":
    main()
