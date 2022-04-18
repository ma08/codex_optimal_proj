


def get_points(card):
    if card[1] == B:
        if card[0] == 'A':
            return 11
        elif card[0] == 'K':
            return 4
        elif card[0] == 'Q':
            return 3
        elif card[0] == 'J':
            return 20
        elif card[0] == 'T':
            return 10
        elif card[0] == '9':
            return 14
    elif card[1] in dominant:
        if card[0] == 'A':
            return 11
        elif card[0] == 'K':
            return 4
        elif card[0] == 'Q':
            return 3
        elif card[0] == 'J':
            return 2
        elif card[0] == 'T':
            return 10


N, B = input().split()
N = int(N)

cards = []
for i in range(N*4):
    cards.append(input().split())

dominant = ['S', 'H', 'D', 'C']
dominant.remove(B)

points = 0
for card in cards:
    points += get_points(card)

print(points)
