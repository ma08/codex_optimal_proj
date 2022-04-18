

N, B = input().split()  # N: number of players, B: trump suit
N = int(N)  # convert string to int

cards = []  # list to store cards
for i in range(4*N):
    cards.append(input())  # input cards

points = 0  # points
for card in cards:
    num = card[0]  # first character
    suit = card[1]  # second character

    if suit == B:  # if suit is trump suit
        if num == 'A':
            points += 4
        elif num == 'K':
            points += 4
        elif num == 'Q':
            points += 3
        elif num == 'J':
            points += 2
        elif num == 'T':
            points += 10
        elif num == '9':
            points += 14
    else:  # if suit is not trump suit
        if num == 'A':
            points += 11
        elif num == 'K':
            points += 4
        elif num == 'Q':
            points += 3
        elif num == 'J':
            points += 20
        elif num == 'T':
            points += 10

print(points)  # output points
