
#-----main-----
N, B = input().split() #get input
N = int(N) #convert to integer
B = str(B) #convert to string

points = 0 #initialize points

for i in range(4*N): #loop through the cards
    card = input() #get input
    number = card[0] #get the number
    suit = card[1] #get the suit
    if suit == B: #if the suit is the trump suit
        if number == 'A': #check the number
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
    else: #if the suit is not the trump suit
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

print(points) #print the points
