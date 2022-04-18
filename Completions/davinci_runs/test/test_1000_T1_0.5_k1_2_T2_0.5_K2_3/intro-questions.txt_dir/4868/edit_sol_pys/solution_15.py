
from sys import stdin, stdout

def solve(white, black):
    board = [["." for _ in range(8)] for _ in range(8)]
    for piece in white.split(","):
        board[int(piece[1]) - 1][ord(piece[0]) - 97] = piece[2].lower()
    for piece in black.split(","):
        board[int(piece[1]) - 1][ord(piece[0]) - 97] = piece[2].upper()
    for line in board:
        stdout.write("+---+---+---+---+---+---+---+---+\n")
        for piece in line:
            stdout.write("|")
            if piece == ".":
                stdout.write(":::")
            else:
                stdout.write(":%s:" % piece)
        stdout.write("|\n")
    stdout.write("+---+---+---+---+---+---+---+---+\n")

def main():
    white = stdin.readline().strip().split(":")[1].strip()
    black = stdin.readline().strip().split(":")[1].strip()
    solve(white, black)

main()
