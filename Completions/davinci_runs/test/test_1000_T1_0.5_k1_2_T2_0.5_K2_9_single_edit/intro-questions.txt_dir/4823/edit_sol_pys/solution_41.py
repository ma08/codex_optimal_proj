

# This solution is a little bit different than the one in the book.
# The book uses a dictionary to keep track of how many of each rank
# there is in the hand. I decided to use a list instead.

# The input is a string with the hand.
hand = input()

# This list will keep track of how many of each rank there is in the hand
handCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# This for loop will add one to the appropriate index of the list
# depending on the rank of the card.
for i in range(0, 5):
    if hand[3*i] == 'A':
        handCount[0] += 1
    elif hand[3*i] == '2':
        handCount[1] += 1
    elif hand[3*i] == '3':
        handCount[2] += 1
    elif hand[3*i] == '4':
        handCount[3] += 1
    elif hand[3*i] == '5':
        handCount[4] += 1
    elif hand[3*i] == '6':
        handCount[5] += 1
    elif hand[3*i] == '7':
        handCount[6] += 1
    elif hand[3*i] == '8':
        handCount[7] += 1
    elif hand[3*i] == '9':
        handCount[8] += 1
    elif hand[3*i] == 'T':
        handCount[9] += 1
    elif hand[3*i] == 'J':
        handCount[10] += 1
    elif hand[3*i] == 'Q':
        handCount[11] += 1
    elif hand[3*i] == 'K':
        handCount[12] += 1

# This for loop will find the maximum value in the handCount list,
# which is the strength of the hand.
strength = 0
for i in range(0, 13):
    if handCount[i] > strength:
        strength = handCount[i]

# The strength is printed.
print(strength)
