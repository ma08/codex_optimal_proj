

N, B = input().split()
N = int(N)

cards = []
for _ in range(N*4):
    cards.append(input().split())

dominants = ['S', 'H', 'D', 'C']
dominants.remove(B)

points = 0
for card in cards:
    if card[1] == B:
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
            points += 14
    elif card[1] in dominants:
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
