

N, B = input().split()
N = int(N)

cards = []
for i in range(N*4):
    cards.append(input().split())

dominant = ['S', 'H', 'D', 'C']
dominant.remove(B)

points = 0
for card in cards:
    if card[1] == B:  # card is a trump
        if card[0] == 'A':  # card is an ace
            points += 11  # add 11 points
        elif card[0] == 'K':  # card is a king
            points += 4  # add 4 points
        elif card[0] == 'Q':  # card is a queen
            points += 3  # add 3 points
        elif card[0] == 'J':  # card is a jack
            points += 20  # add 20 points
        elif card[0] == 'T':  # card is a 10
            points += 10  # add 10 points
        elif card[0] == '9':  # card is a 9
            points += 14  # add 14 points
    elif card[1] in dominant:  # card is a dominant
        if card[0] == 'A':  # card is an ace
            points += 11  # add 11 points
        elif card[0] == 'K':  # card is a king
            points += 4  # add 4 points
        elif card[0] == 'Q':  # card is a queen
            points += 3  # add 3 points
        elif card[0] == 'J':  # card is a jack
            points += 2  # add 2 points
        elif card[0] == 'T':  # card is a 10
            points += 10  # add 10 points

print(points)
