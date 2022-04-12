

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
    for peace in "KQRBNP":
        if peace in peaces:
            if peace.isupper():
                # White piece.
                white += peace
                white += chr(ord('a') + peaces[peace][1])
                white += str(8 - peaces[peace][0])
                white += ","
            else:
                # Black piece.
                black += peace.upper()
                black += chr(ord('a') + peaces[peace][1])
                black += str(8 - peaces[peace][0])
                black += ","

    # Remove the last comma and print.
    print(white[:-1])
    print(black[:-1])

if __name__ == '__main__':
    main()
