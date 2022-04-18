

# Get input
numWords = int(input())
words = []
for i in range(numWords):
    words.append(input())

# Check if the game was played according to the rules
fairGame = True
for i in range(1, numWords):
    if words[i][0] != words[i-1][-1]:
        fairGame = False
        break

if fairGame:
    print("Fair Game")
else:
    print("Player " + str(i+1) + " lost")
