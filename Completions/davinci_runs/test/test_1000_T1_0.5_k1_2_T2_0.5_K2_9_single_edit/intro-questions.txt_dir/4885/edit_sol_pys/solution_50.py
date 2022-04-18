

def main():
    """
    Main function.
    """
    # Read input.
    board = []
    for _ in range(0, 8):
        board.append(input())

    # Find the pieces.
    pieces = {}
    for row in range(0, 8):
        for col in range(0, 8):
            if board[row][col] != "." and board[row][col] != ":":
                pieces[board[row][col]] = (row, col)

    # Print the output.
    white = "White: "
    black = "Black: "
    for piece in "KQRBNP":
        if piece in pieces:
            if piece.isupper():
                # White piece.
                white += piece
                white += chr(ord('a') + pieces[piece][1])
                white += str(8 - pieces[piece][0])
                white += ","
            else:
                # Black piece.
                black += (piece.upper() + chr(ord('a') + pieces[piece][1]) + str(8 - pieces[piece][0]) + ",")

    # Remove the last comma and print.
    print(white[:-1])
    print(black[:-1])

if __name__ == '__main__':
    main()
