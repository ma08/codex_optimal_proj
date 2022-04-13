
# Get the input
n = int(input())
a = []
for i in range(n):
    a.append(input())

# Check if the game was played according to the rules
fairGame = True
for i in range(1, n):
    if a[i][0] != a[i-1][-1]:
        fairGame = False
        break

if fairGame:
    print("Fair Game")
else:
    print("Player " + str(i) + " lost")
