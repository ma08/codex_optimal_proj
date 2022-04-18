

from sys import stdin, stdout

def solve(white, black):
    board = [["."] * 8 for i in range(8)]
    for piece in white.split(","):
        board[int(piece[2]) - 1][ord(piece[1]) - 97] = piece[0].lower()
    for piece in black.split(","):
        board[int(piece[2]) - 1][ord(piece[1]) - 97] = piece[0].upper()
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
