

N, B = input().split()  # N is the number of cards in the deck and B is the trump suit
N = int(N)  # convert N to an integer

cards = []  # create an empty list to hold the cards
for i in range(N*4):  # loop through the cards
    cards.append(input().split())  # add the cards to the list

dominant = ['S', 'H', 'D', 'C']  # create a list of the dominant suits
dominant.remove(B)  # remove the trump suit from the list

points = 0  # create a variable to hold the points
for card in cards:  # loop through the cards
    if card[1] == B:  # if the card is in the trump suit
        if card[0] == 'A':  # if the card is an ace
            points += 11  # add 11 points
        elif card[0] == 'K':  # if the card is a king
            points += 4  # add 4 points
        elif card[0] == 'Q':  # if the card is a queen
            points += 3  # add 3 points
        elif card[0] == 'J':  # if the card is a jack
            points += 20  # add 20 points
        elif card[0] == 'T':  # if the card is a ten
            points += 10  # add 10 points
        elif card[0] == '9':  # if the card is a nine
            points += 0  # add 0 points
    elif card[1] in dominant:  # if the card is in a dominant suit
        if card[0] == 'A':  # if the card is an ace
            points += 11  # add 11 points
        elif card[0] == 'K':  # if the card is a king
            points += 4  # add 4 points
        elif card[0] == 'Q':  # if the card is a queen
            points += 3  # add 3 points
        elif card[0] == 'J':  # if the card is a jack
            points += 2  # add 2 points
        elif card[0] == 'T':  # if the card is a ten
            points += 10  # add 10 points

print(points)
