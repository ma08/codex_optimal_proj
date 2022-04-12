

from sys import stdin, stdout

def solve(white_pieces, black_pieces):
    board = [["." for i in range(8)] for j in range(8)]
    for piece in white_pieces.split(","):
        board[int(piece[2]) - 1][ord(piece[1]) - 97] = piece[0]
    for piece in black_pieces.split(","):
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
    white_pieces = stdin.readline().strip().split(":")[1].strip()
    black_pieces = stdin.readline().strip().split(":")[1].strip()
    solve(white_pieces, black_pieces)

main()
