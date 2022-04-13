
n, b = input().split()
n = int(n)

cards = []
for i in range(4 * n):
    cards.append(input())

points = 0
for card in cards:
    num = card[0]
    suit = card[1]

    if suit == b:
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
        elif num == '9':
            points += 14
    else:
        if num == 'A':
            points += 11
        elif num == 'K':
            points += 4
        elif num == 'Q':
            points += 3
        elif num == 'J':
            points += 2
        elif num == 'T':
            points += 10

print(points)
