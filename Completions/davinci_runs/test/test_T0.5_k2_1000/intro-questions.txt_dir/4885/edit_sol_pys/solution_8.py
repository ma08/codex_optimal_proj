

def main():
    """
    Main function.
    """
    # Read input.
    board = []
    for _ in range(0, 8):
        board.append(input())

    # Find the peaces.
    peaces = {}
    for row in range(0, 8):
        for col in range(0, 8):
            if board[row][col] != "." and board[row][col] != ":":
                peaces[board[row][col]] = (row, col)

    # Print the output.
    white = "White: "
    black = "Black: "
    for piece in "KQRBNP":
        if piece in peaces:
            if piece.isupper():
                # White piece.
                white += piece
                white += chr(ord('a') + peaces[piece][1])
                white += str(8 - peaces[piece][0])
                white += ","
            else:
                # Black piece.
                black += piece.upper()
                black += chr(ord('a') + peaces[piece][1])
                black += str(8 - peaces[piece][0])
                black += ","

    # Remove the last comma and print.
    print(white[:-1])
    print(black[:-1])

if __name__ == '__main__':
    main()
