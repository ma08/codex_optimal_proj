
#-----main-----
#-----main-----
N, B = input().split()
N = int(N)
B = str(B)

points = 0

for i in range(4*N):
    card = input()
    number = card[0]
    suit = card[1]
    if suit == B:
        if number == 'A':
            points += 11
        elif number == 'K':
            points += 4
        elif number == 'Q':
            points += 3
        elif number == 'J':
            points += 20
        elif number == 'T':
            points += 10
        elif number == '9':
            points += 14
        elif number == '8':
            points += 0
        elif number == '7':
            points += 0
    else:
        if number == 'A':
            points += 11
        elif number == 'K':
            points += 4
        elif number == 'Q':
            points += 3
        elif number == 'J':
            points += 2
        elif number == 'T':
            points += 10
        elif number == '9':
            points += 0
        elif number == '8':
            points += 0
        elif number == '7':
            points += 0

print(points)
