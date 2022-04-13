
from sys import stdin, stdout

def solve(white, black):
    board = [["."] * 8 for j in range(8)]
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

if __name__ == "__main__":
    main()
