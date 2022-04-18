

#Solution

n, b = input().split()
n = int(n)
b = b.upper()
points = 0

for i in range(4*n):
    card, suit = input().split() # input is stored in card and suit as string
    suit = suit.upper() # change suit to uppercase
    if suit == b: # check if suit is same as trump
        if card == "A":
            points += 11
        elif card == "K":
            points += 4
        elif card == "Q":
            points += 3
        elif card == "J":
            points += 20
        elif card == "T":
            points += 10
        elif card == "9":
            points += 14
    else: # if suit is not trump
        if card == "A":
            points += 11
        elif card == "K":
            points += 4
        elif card == "Q":
            points += 3
        elif card == "J":
            points += 2
        elif card == "T":
            points += 10
print(points) # print points
