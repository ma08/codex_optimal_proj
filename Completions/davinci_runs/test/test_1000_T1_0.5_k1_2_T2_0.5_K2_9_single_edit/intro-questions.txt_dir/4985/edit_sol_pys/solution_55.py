

#-----main-----

# input
n = int(input())
b = input()

# initialize variables
hands = []
total = 0

# loop to create hands
for i in range(n):
    hand = []
    for j in range(4):
        hand.append(input())
    hands.append(hand)

# loop to calculate total
for hand in hands:
    for card in hand:
        # determine score
        if card[0] == 'A':
            if card[1] == b:
                score = 11
            else:
                score = 11
        elif card[0] == 'K':
            if card[1] == b:
                score = 4
            else:
                score = 4
        elif card[0] == 'Q':
            if card[1] == b:
                score = 3
            else:
                score = 3
        elif card[0] == 'J':
            if card[1] == b:
                score = 20
            else:
                score = 2
        elif card[0] == 'T':
            if card[1] == b:
                score = 10
            else:
                score = 10
        elif card[0] == '9':
            if card[1] == b:
                score = 14
            else:
                score = 0
        elif card[0] == '8' and card[1] == b:
            score = 0
        elif card[0] == '7' and card[1] == b:
            score = 0
        # add to total
        total += score

# print
print(total)
