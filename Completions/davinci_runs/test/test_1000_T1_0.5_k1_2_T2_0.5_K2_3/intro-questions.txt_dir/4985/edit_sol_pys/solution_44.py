

#Solution
#take input
n, b = input().split()
n = int(n)
b = b.upper()
points = 0
#loop for 4*n times

    #take input
for i in range(4*n):
    card, suit = input().split()
    #if suit is equal to trump
    suit = suit.upper()
            #if card is ace
    if suit == b:
        if card == "A":
            #if card is king
            points += 11
        elif card == "K":
            #if card is queen
            points += 4
        elif card == "Q":
            #if card is jack
            points += 3
        elif card == "J":
            points += 20
            #if card is 10
        elif card == "T":
            points += 10
            #if card is 9
        elif card == "9":
            points += 14
    else:
        #if card is ace
        if card == "A":
            points += 11
        #if card is king
        elif card == "K":
            points += 4
        #if card is queen
        elif card == "Q":
            points += 3
        #if card is jack
        elif card == "J":
            points += 2
        #if card is 10
        elif card == "T":
            points += 10
#print the points
print(points)
