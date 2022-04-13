
#-----main-----

# input
n = int(input()) # number of hands
b = input() # trump

# initialize variables
hands = [] # list of hands
total = 0 # total score

# loop to create hands
for i in range(n):
    hand = [] # hand
    for j in range(4):
        hand.append(input())
    hands.append(hand) # add hand to hands

# loop to calculate total
for hand in hands:
    for card in hand:
        # determine score of card
        if card[0] == 'A':
            if card[1] == b:
                score = 11
            else:
                score = 1
        elif card[0] == 'K':
            if card[1] == b:
                score = 4
            else:
                score = 0
        elif card[0] == 'Q':
            if card[1] == b:
                score = 3
            else:
                score = 0
        elif card[0] == 'J':
            if card[1] == b:
                score = 20
            else:
                score = 0
        elif card[0] == 'T':
            if card[1] == b:
                score = 10
            else:
                score = 0
        elif card[0] == '9':
            if card[1] == b:
                score = 14
            else:
                score = 0
        elif card[0] == '8':
            score = 0
        elif card[0] == '7':
            score = 0
        # add score of card to total
        total += score 

# print
print(total)
