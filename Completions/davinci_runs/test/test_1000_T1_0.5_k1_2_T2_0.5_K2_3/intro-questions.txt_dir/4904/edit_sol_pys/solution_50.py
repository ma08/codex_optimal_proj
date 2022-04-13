
# Gets the input from the user
record = input()

# Initializes the scores to zero
score_a = 0
score_b = 0

# Loops through the input, adding the scores to the appropriate player
for i in range(1, len(record), 2):
    if record[i] == "A":
        score_a += int(record[i])
    elif record[i] == "B":
        score_b += int(record[i])

# Prints the winner
if score_a > score_b:
    print("A")
else:
    print("B")
