

#Card class
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def getValue(self):
        return self.value
    def getSuit(self):
        return self.suit

#read input
input = input().split()
N = int(input[0])
dominantSuit = input[1]
cards = []
for i in range(4*N):
    input = input().split()
    value = input[0]
    suit = input[1]
    card = Card(value, suit) #create card
    cards.append(card) #add card to list

#calculate score
score = 0

for card in cards:
    if card.getValue() == "A":
        if card.getSuit() == dominantSuit:
            score += 11
        else:
            score += 11
    elif card.getValue() == "K":
        if card.getSuit() == dominantSuit:
            score += 4
        else:
            score += 4
    elif card.getValue() == "Q":
        if card.getSuit() == dominantSuit:
            score += 3
        else:
            score += 3
    elif card.getValue() == "J":
        if card.getSuit() == dominantSuit:
            score += 20
        else:
            score += 2
    elif card.getValue() == "T":
        if card.getSuit() == dominantSuit:
            score += 10
        else:
            score += 10
    elif card.getValue() == "9":
        if card.getSuit() == dominantSuit:
            score += 14
        else:
            score += 0
    elif card.getValue() == "8":
        if card.getSuit() == dominantSuit:
            score += 0
        else:
            score += 0
    elif card.getValue() == "7":
        if card.getSuit() == dominantSuit:
            score += 0
        else:
            score += 0

print(score)
