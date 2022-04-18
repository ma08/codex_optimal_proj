

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
        if number == 'A' or number == 'K' or number == 'Q' or number == 'J' or number == 'T':
            points += 10
        elif number == '9':
            points += 13
    else:
        if number == 'A' or number == 'K' or number == 'Q' or number == 'J' or number == 'T':
            points += 10

print(points)
