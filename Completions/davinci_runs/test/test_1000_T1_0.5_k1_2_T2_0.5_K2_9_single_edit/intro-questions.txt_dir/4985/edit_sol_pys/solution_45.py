

#-----main-----#

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
        if card[0] == 'A': score = 11
        elif card[0] == 'K': score = 4
        elif card[0] == 'Q': score = 3
        elif card[0] == 'J': score = 2
        elif card[0] == 'T': score = 10
        elif card[0] == '9': score = 0
        elif card[0] == '8': score = 0
        elif card[0] == '7': score = 0
        # double score if trump
        if card[1] == b: score *= 2
        # add to total
        total += score

# print
print(total)
