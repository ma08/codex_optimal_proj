

def main():
    """
    This function is the main function of this program.

    This function reads the number of pieces and the values of the pieces from the input.
    Then, it prints the total value of Alice's pieces and the total value of Bob's pieces.

    This function uses the function choose_piece() to choose the piece to take.
    """
    # Read the number of pieces.
    n = int(input())

    # Read the values of the pieces.
    pieces = [int(a) for a in input().split()]

    # Initialize the total value of Alice's pieces and the total value of Bob's pieces.
    alice_total = 0
    bob_total = 0

    # Loop through all the pieces.
    for i in range(n):
        # Check if it is Alice's turn.
        if i % 2 == 0:
            # Choose the piece for Alice.
            alice_piece = choose_piece(pieces)

            # Add the value of Alice's piece to the total value of Alice's pieces.
            alice_total += alice_piece

            # Remove the chosen piece from the list of pieces.
            pieces.remove(alice_piece)
        # Check if it is Bob's turn.
        else:
            # Choose the piece for Bob.
            bob_piece = choose_piece(pieces)

            # Add the value of Bob's piece to the total value of Bob's pieces.
            bob_total += bob_piece

            # Remove the chosen piece from the list of pieces.
            pieces.remove(bob_piece)

    # Print the total value of Alice's pieces and the total value of Bob's pieces.
    print("{} {}".format(alice_total, bob_total))

def choose_piece(pieces):
    """
    This function chooses a piece to take.

    This function takes a list of pieces as the parameter.
    It returns the value of the chosen piece.
    """
    # Initialize the maximum value of the chosen piece.
    max_piece = 0

    # Loop through all the pieces.
    for piece in pieces:
        # Check if the value of the piece is greater than the maximum value of the chosen piece.
        if piece > max_piece:
            # Set the value of the piece as the new maximum value of the chosen piece.
            max_piece = piece

    # Return the maximum value of the chosen piece.
    return max_piece

# Call the main function.
main()