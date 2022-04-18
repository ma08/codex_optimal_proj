

from sys import stdin

def solve(white, black):
    board = [["." for i in range(8)] for j in range(8)]
    for piece in white.split(","):
        board[int(piece[2]) - 1][ord(piece[1]) - 97] = piece[0].lower()
    for piece in black.split(","):
        board[int(piece[2]) - 1][ord(piece[1]) - 97] = piece[0].upper()
    for line in board:
        print("+---+---+---+---+---+---+---+---+")
        for piece in line:
            print("|", end="")
            if piece == ".":
                print(":::", end="")
            else:
                print(":%s:" % piece, end="")
        print("|")
    print("+---+---+---+---+---+---+---+---+")

def main():
    white = stdin.readline().strip().split(":")[1].strip().lower()
    black = stdin.readline().strip().split(":")[1].strip().lower()
    solve(white, black)

main()
