


class Piece:
    def __init__(self, color, kind, x, y):
        self.color = color
        self.kind = kind
        self.x = x
        self.y = y

    def __str__(self):
        return self.color + self.kind + chr(97 + self.x) + str(self.y + 1)
from sys import stdin, stdout

def solve(white, black):
    board = [["." for i in range(8)] for j in range(8)]
    for piece in white.split(","):
        board[int(piece[2]) - 1][ord(piece[1]) - 97] = Piece(piece[0].lower(), piece[1], ord(piece[2]) - 97, int(piece[3]) - 1)
    for piece in black.split(","):
        board[int(piece[2]) - 1][ord(piece[1]) - 97] = Piece(piece[0].upper(), piece[1], ord(piece[2]) - 97, int(piece[3]) - 1)
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
