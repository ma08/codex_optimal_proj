
#-----main-----#

N, B = input().split()
N = int(N)

points = 0

for i in range(4*N):
    card = input()
    number = card[0]
    suit = card[1]

    if number == 'A':
        points += 11
    elif number == 'K':
        points += 4
    elif number == 'Q':
        points += 3
    elif number == 'J':
        if suit == B:
            points += 20
        else:
            points += 2
    elif number == 'T':
        points += 10
    elif number == '9':
        if suit == B:
            points += 14
    elif number == '8':
        pass
    elif number == '7':
        pass

print(points)
