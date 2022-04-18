

N, B = input().strip().split()
N = int(N)  # number of players
B = B  # trump suit

cards = []
for _ in range(N*4):
    cards.append(input().strip().split())

dominant_suits = ['S', 'H', 'D', 'C']
print(dominant_suits)
dominant_suits.remove(B)

points = 0
for card in cards:
    if card[1] == B:  # if the suit is trump
        if card[0] == 'A':  # if the card is ace
            points += 11  # add 11 points
        elif card[0] == 'K':  # if the card is king
            points += 4  # add 4 points
        elif card[0] == 'Q':  # if the card is queen
            points += 3  # add 3 points
        elif card[0] == 'J':  # if the card is jack
            points += 20  # add 20 points
        elif card[0] == 'T':  # if the card is 10
            points += 10  # add 10 points
        elif card[0] == '9':  # if the card is 9
            points += 14  # add 14 points
    elif card[1] in dominant_suits:  # if the suit is dominant
        if card[0] == 'A':  # if the card is ace
            points += 11  # add 11 points
        elif card[0] == 'K':  # if the card is king
            points += 4  # add 4 points
        elif card[0] == 'Q':  # if the card is queen
            points += 3  # add 3 points
        elif card[0] == 'J':  # if the card is jack
            points += 2  # add 2 points
        elif card[0] == 'T':  # if the card is 10
            points += 10  # add 10 points

print(points)
