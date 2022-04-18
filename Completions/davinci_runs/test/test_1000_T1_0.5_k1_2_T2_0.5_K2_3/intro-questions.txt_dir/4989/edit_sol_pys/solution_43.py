
def main():
    """
    This function is the main function of this program.

    This function reads the number of cards and the values of the cards from the input.
    Then, it prints the total value of Alice's cards and the total value of Bob's cards.

    This function uses the function choose_card() to choose the card to take.
    """
    # Read the number of cards.
    n = int(input())

    # Read the values of the cards.
    cards = [int(a) for a in input().split()]

    # Initialize the total value of Alice's cards and the total value of Bob's cards.
    alice_total = 0
    bob_total = 0

    # Loop through all the cards.
    for i in range(n):
        # Check if it is Alice's turn.
        if i % 2 == 0:
            # Choose the card for Alice.
            alice_card = choose_card(cards)

            # Add the value of Alice's card to the total value of Alice's cards.
            alice_total += alice_card

            # Remove the chosen card from the list of cards.
            cards.remove(alice_card)
        # Check if it is Bob's turn.
        else:
            # Choose the card for Bob.
            bob_card = choose_card(cards)

            # Add the value of Bob's card to the total value of Bob's cards.
            bob_total += bob_card

            # Remove the chosen card from the list of cards.
            cards.remove(bob_card)


    # Print the total value of Alice's cards and the total value of Bob's cards.
    print("{} {}".format(alice_total, bob_total))

def choose_card(cards):
    """
    This function chooses a card to take.

    This function takes a list of cards as the parameter.
    It returns the value of the chosen card.
    """
    # Initialize the maximum value of the chosen card.
    max_card = 0

    # Loop through all the cards.
    for card in cards:
        # Check if the value of the card is greater than the maximum value of the chosen card.
        if card > max_card:
            # Set the value of the card as the new maximum value of the chosen card.
            max_card = card

    # Return the maximum value of the chosen card.
    return max_card

# Call the main function.
main()
