

N, B = input().split() # N = number of cards, B = trump suit
N = int(N) # convert N to integer

cards = []
for i in range(N*4):
    cards.append(input().split()) # append cards to list

dominant = ['S', 'H', 'D', 'C'] # list of dominant suits
dominant.remove(B) # remove trump suit from list of dominant suits

points = 0
for card in cards:
    if card[1] == B: # if card is trump suit
        if card[0] == 'A':
            points += 11
        elif card[0] == 'K':
            points += 4
        elif card[0] == 'Q':
            points += 3
        elif card[0] == 'J':
            points += 20
        elif card[0] == 'T':
            points += 10
        elif card[0] == '9':
            points += 0
    elif card[1] in dominant: # if card is dominant suit
        if card[0] == 'A':
            points += 11
        elif card[0] == 'K':
            points += 4
        elif card[0] == 'Q':
            points += 3
        elif card[0] == 'J':
            points += 2
        elif card[0] == 'T':
            points += 10

print(points)
